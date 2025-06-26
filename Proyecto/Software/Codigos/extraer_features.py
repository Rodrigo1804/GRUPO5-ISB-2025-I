#!/usr/bin/env python3
# extract_features.py

import os
import glob
import numpy as np
import pandas as pd
from scipy.signal import welch

# --- Parámetros de ventana y señal ---
FS       = 1000      # Hz
WIN_S    = 5         # segundos
OVERLAP  = 0.5       # 50%
ZC_THR   = 0.01      # umbral para ZC & WAMP

# --- Directorios de entrada y archivos de salida ---
MUSCLE_DIRS = {
    "flexor":  "musculos_emg_filtrado/Flexor_Filtradas",
    "extensor":"musculos_emg_filtrado/Extensor_Filtradas"
}

# --- Funciones auxiliares ---
def segmentar(signal, fs=FS, win_s=WIN_S, overlap=OVERLAP):
    Nwin = int(win_s * fs)
    step = int(Nwin * (1 - overlap))
    return [ signal[i:i+Nwin]
             for i in range(0, len(signal)-Nwin+1, step) ]

def features_tiempo(seg, zc_thr=ZC_THR):
    rms  = np.sqrt(np.mean(seg**2))
    mav  = np.mean(np.abs(seg))
    wl   = np.sum(np.abs(np.diff(seg)))
    zc   = np.sum(((seg[:-1]*seg[1:])<0) & (np.abs(np.diff(seg))>zc_thr))
    ssc  = np.sum(((seg[1:-1]-seg[:-2])*(seg[1:-1]-seg[2:])>0))
    wamp = np.sum(np.abs(np.diff(seg)) > zc_thr)
    return rms, mav, wl, zc, ssc, wamp

def features_frecuencia(seg, fs=FS):
    f, Pxx = welch(seg, fs=fs, nperseg=fs*2)
    Pcum   = np.cumsum(Pxx)
    total  = Pcum[-1]
    mdf    = f[np.searchsorted(Pcum, total/2)]
    mnf    = np.sum(f * Pxx) / total
    return mnf, mdf, total

# --- Bucle principal sobre músculos ---
for muscle, input_dir in MUSCLE_DIRS.items():
    rows = []
    input_dir = os.path.expanduser(input_dir)
    csv_files = glob.glob(os.path.join(input_dir, "*.csv"))
    print(f">> [{muscle}] encontradas {len(csv_files)} señales en {input_dir}")

    for fp in csv_files:
        fn = os.path.basename(fp)
        try:
            sujeto, condicion, _ = fn.split("_", 2)
        except ValueError:
            print(f"   ⚠️ nombre inesperado: {fn}, saltando")
            continue

        df = pd.read_csv(fp)
        if "EMG_mV_filtrado" not in df.columns:
            print(f"   ❌ falta columna EMG_mV_filtrado en {fn}")
            continue

        sig = df["EMG_mV_filtrado"].values
        if len(sig) < FS * WIN_S:
            print(f"   ⚠️ señal muy corta ({len(sig)} muestras) en {fn}")
            continue

        segs = segmentar(sig)
        print(f"   → {fn}: {len(segs)} ventanas")
        for i, seg in enumerate(segs, 1):
            rms, mav, wl, zc, ssc, wamp = features_tiempo(seg)
            mnf, mdf, power = features_frecuencia(seg)
            rows.append({
                "sujeto":    sujeto,
                "condicion": condicion,
                "ventana":   i,
                "RMS":       rms,
                "MAV":       mav,
                "WL":        wl,
                "ZC":        zc,
                "SSC":       ssc,
                "WAMP":      wamp,
                "MNF":       mnf,
                "MDF":       mdf,
                "Power":     power
            })

    out_csv = f"features_{muscle}.csv"
    pd.DataFrame(rows).to_csv(out_csv, index=False)
    print(f">> [{muscle}] guardado {len(rows)} filas en {out_csv}\n")

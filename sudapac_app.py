# -*- coding: utf-8 -*-
"""
Sudapac OS v1.1 — المحرك الرئيسي والمشغل للأنومة الموزعة
"""

import sys
import os
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

def _try_import(module_name: str):
    try: return __import__(module_name), None
    except Exception as exc: return None, f"{type(exc).__name__}: {exc}"

_broker_mod, _e_broker = _try_import("sudapac_ksa_broker")
_voice_mod, _e_voice = _try_import("sudapac_voice_pipeline")
_invoice_mod, _e_invoice = _try_import("sudapac_invoice_backend")

def run_demo() -> int:
    print("╔══════════════════════════════════════════════════════╗")
    print("║        SUDAPAC — منصة الوجيستيات الذكية (v1.1)       ║")
    print("╚══════════════════════════════════════════════════════╝\n")
    
    if not all([_broker_mod, _voice_mod, _invoice_mod]):
        print("❌ خطأ: بعض الملفات المنفصلة مفقودة في المجلد الحالي.")
        return 1

    # 1. اختبار بوابة المستودع وكرت التشغيل
    broker = _broker_mod.KSAGovernmentBroker()
    gate = broker.warehouse_gate_check("1098765432", "1234 أ ب ج", "8837162")
    
    if gate.allowed:
        print(f"🛂 [TGA]: كرت التشغيل ساري ومطابق لمواصفات وزارة النقل: {gate.operating_card.vehicle_type}")
        print(f"✅ [Gate]: الدخول مسموح للسائق: {gate.driver_name}")
    
    # 2. اختبار موديول الصوت
    voice = _voice_mod.VoicePipeline()
    call = _voice_mod.DriverCall(driver_id="DRV-112", driver_name="أبو فهد", audio_ref="البوابة ٣ زحمة حوالي ٤٠ دقيقة", lat=24.81, lng=46.64)
    vp = voice.handle_call(call)
    print(f"🎙️ [Voice]: تحليل المكالمة: {vp.transcript.text} -> الرد: {vp.intent.response_text}")
    
    return 0

if __name__ == "__main__":
    sys.exit(run_demo())

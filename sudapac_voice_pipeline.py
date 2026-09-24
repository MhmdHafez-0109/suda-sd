# -*- coding: utf-8 -*-
"""
Sudapac Voice Pipeline — موديول معالجة خط الصوت الحي والتحليل النفسي الدلالي
"""

from enum import Enum
from dataclasses import dataclass, asdict

class DriverEmotion(Enum):
    CALM = "هادئ"
    FRUSTRATED = "غاضب / متوتر"
    URGENT = "مستعجل جداً"

class LogisticsIntent(Enum):
    TRAFFIC_DELAY = "تأخير بسبب الازدحام"
    GATE_BLOCKED = "البوابة مغلقة / زحمة بالمستودع"
    UNKNOWN = "غير محدد"

@dataclass
class VoiceTranscript: text: str; language: str; confidence: float
@dataclass
class IntentAnalysis: intent: LogisticsIntent; confidence: float; response_text: str
@dataclass
class SentimentAnalysis: emotion: DriverEmotion; score: float
@dataclass
class EscalationOrder: flag_for_human: bool; reason: str; priority: str

@dataclass
class ProcessedCallReport:
    transcript: VoiceTranscript; intent: IntentAnalysis; sentiment: SentimentAnalysis; escalation_order: EscalationOrder or None
    def to_dict(self):
        return {
            "transcript": asdict(self.transcript),
            "intent": {"intent": self.intent.intent.value, "confidence": self.intent.confidence, "response_text": self.intent.response_text},
            "sentiment": {"emotion": self.sentiment.emotion.value, "score": self.sentiment.score},
            "escalation_order": asdict(self.escalation_order) if self.escalation_order else None
        }

@dataclass
class DriverCall: driver_id: str; driver_name: str; audio_ref: str; lat: float; lng: float

class VoicePipeline:
    def handle_call(self, call_obj) -> ProcessedCallReport:
        transcript = VoiceTranscript(text=call_obj.audio_ref, language="ar", confidence=0.98)
        intent = IntentAnalysis(intent=LogisticsIntent.GATE_BLOCKED, confidence=0.95, response_text="علم يا كابتن، تم رصد التكدس وإبلاغ ساحة المستودع.")
        sentiment = SentimentAnalysis(emotion=DriverEmotion.CALM, score=0.5)
        return ProcessedCallReport(transcript=transcript, intent=intent, sentiment=sentiment, escalation_order=None)

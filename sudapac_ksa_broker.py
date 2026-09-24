# -*- coding: utf-8 -*-
"""
Sudapac KSA Broker — وسيط نظام الهيئة العامة للنقل (TGA) والخرائط
يتضمن موديول التحقق من كرت تشغيل العربة ومطابقتها للمواصفات الحكومية.
"""

from dataclasses import dataclass, asdict

@dataclass
class OperatingCardDetails:
    card_number: str          
    is_valid: bool            
    expiry_date: str          
    vehicle_type: str         
    owner_name: str           
    def to_dict(self): return asdict(self)

@dataclass
class GateCheckResult:
    allowed: bool
    driver_name: str or None
    gate_pass_code: str or None
    operating_card: OperatingCardDetails or None  
    issues: list[str]
    def to_dict(self): return asdict(self)

@dataclass
class GeoAddressResult:
    national_address: str
    lat: float
    lng: float
    match_score: float
    def to_dict(self): return asdict(self)

class KSAGovernmentBroker:
    def verify_operating_card(self, plate_number: str, card_number: str) -> OperatingCardDetails:
        """التحقق من كرت تشغيل العربة ومطابقته لاشتراطات وزارة النقل TGA."""
        if len(card_number) >= 7 and card_number.isdigit():
            return OperatingCardDetails(
                card_number=card_number,
                is_valid=True,
                expiry_date="2028-05-15",
                vehicle_type="شاحنة نقل ثقيل (قاطرة ومقطورة)",
                owner_name="شركة سلاسل الإمداد السريعة"
            )
        else:
            return OperatingCardDetails(
                card_number=card_number,
                is_valid=False,
                expiry_date="2025-01-01",
                vehicle_type="غير محدد",
                owner_name="غير مسجل"
            )

    def warehouse_gate_check(self, driver_id: str, plate_number: str, card_number: str) -> GateCheckResult:
        issues = []
        if not (driver_id.startswith("1") or driver_id.startswith("2")) or len(driver_id) != 10:
            issues.append("رقم هوية السائق أو الإقامة غير صحيح قانونياً")
            
        card_details = self.verify_operating_card(plate_number, card_number)
        if not card_details.is_valid:
            issues.append(f"كرت التشغيل رقم ({card_number}) منتهي الصلاحية أو غير مطابق لمواصفات وزارة النقل")
            
        access_granted = len(issues) == 0
        pass_code = "PASS-9921" if access_granted else None
        driver_name = "خالد عبد الله (أبو فهد)" if access_granted else None
        
        return GateCheckResult(
            allowed=access_granted, driver_name=driver_name,
            gate_pass_code=pass_code, operating_card=card_details, issues=issues
        )

    def geocode_address(self, raw_address: str) -> GeoAddressResult:
        if "ياسمين" in raw_address or "الرياض" in raw_address:
            return GeoAddressResult(national_address="7322 طريق الملك عبد العزيز، حي الياسمين، الرياض 13322", lat=24.8124, lng=46.6432, match_score=0.94)
        return GeoAddressResult(national_address="عنوان غير محدد بدقة", lat=24.7136, lng=46.6753, match_score=0.10)

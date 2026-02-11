from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple, Optional
from rules import ESSENTIAL_CATEGORIES, ACTIVE_INGREDIENTS, ALIAS_MAP, CATEGORY_WEIGHTS, WEEKLY_BUDGET  
AM="am"
PM="pm"
AM_PM="am_pm"
Days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
Strong_Actives={"retinol","aha","bha"}

@dataclass
class PlanResult:
    missing_essentials: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

            
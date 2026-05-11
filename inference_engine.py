"""
Inference Engine — Forward Chaining for Career Counseling
KRR Concept: Facts → Rules → Conclusions
"""

from knowledge_base import KNOWLEDGE_BASE


def run_inference_engine(user_facts: dict) -> list:
    """
    Forward Chaining Inference Engine.
    
    Process:
    1. Take user facts (skills, interests, personality, CGPA)
    2. Compare against each career rule in the Knowledge Base
    3. Calculate match percentage (score / max_score * 100)
    4. Return ranked career list
    """
    results = []

    for career, rules in KNOWLEDGE_BASE.items():
        score      = 0
        max_score  = 0
        reasons    = []
        missing    = []

        # ── Rule 1: CGPA Check (weight: 10) ──────────────────
        max_score += 10
        cgpa = user_facts.get("cgpa", 0.0)
        if cgpa >= rules["min_cgpa"]:
            score += 10
            reasons.append(f"CGPA {cgpa:.1f} meets requirement (min: {rules['min_cgpa']})")
        else:
            reasons_neg = f"CGPA {cgpa:.1f} is below minimum {rules['min_cgpa']}"
            missing.append(f"Improve CGPA to at least {rules['min_cgpa']}")

        # ── Rule 2: Required Skills (weight: 15 each) ─────────
        for skill in rules["required_skills"]:
            max_score += 15
            if skill in user_facts.get("skills", []):
                score += 15
                reasons.append(f"Has required skill: {skill}")
            else:
                missing.append(f"Skill: {skill}")

        # ── Rule 3: Required Interests (weight: 12 each) ──────
        for interest in rules["required_interests"]:
            max_score += 12
            if interest in user_facts.get("interests", []):
                score += 12
                reasons.append(f"Interested in: {interest}")
            else:
                missing.append(f"Interest area: {interest}")

        # ── Rule 4: Personality Bonus (weight: 5 each) ────────
        for trait in rules["personality_bonus"]:
            max_score += 5
            if trait in user_facts.get("personality", []):
                score += 5
                reasons.append(f"Personality match: {trait}")

        # ── Calculate percentage ───────────────────────────────
        pct = round((score / max_score) * 100, 1) if max_score > 0 else 0
        pct = max(0.0, min(100.0, pct))

        # ── Matched vs missing skills ──────────────────────────
        user_skills = user_facts.get("skills", [])
        matched_skills = [s for s in rules["required_skills"] if s in user_skills]
        gap_skills     = [s for s in rules["required_skills"] if s not in user_skills]

        user_interests = user_facts.get("interests", [])
        matched_interests = [i for i in rules["required_interests"] if i in user_interests]
        gap_interests     = [i for i in rules["required_interests"] if i not in user_interests]

        results.append({
            "career":            career,
            "percentage":        pct,
            "score":             score,
            "max_score":         max_score,
            "reasons":           reasons,
            "missing":           missing,
            "matched_skills":    matched_skills,
            "gap_skills":        gap_skills,
            "matched_interests": matched_interests,
            "gap_interests":     gap_interests,
            "rules":             rules,
        })

    results.sort(key=lambda x: x["percentage"], reverse=True)
    return results


def get_domain_filtered(results: list, domain: str) -> list:
    """Filter results by career domain."""
    if domain == "All":
        return results
    return [r for r in results if domain in r["rules"]["domains"]]

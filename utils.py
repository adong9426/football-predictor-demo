weights = {"进攻":0.25, "防守":0.25, "状态":0.2, "主/客场":0.2, "阵容完整性":0.1}

def weighted_score(scores, weights=weights):
    return sum(scores[k] * weights[k] for k in weights)

def rate_team(stats):
    score = {}
    score["进攻"] = 2 if stats["avg_goals"] > 1.7 else 1 if stats["avg_goals"] > 1.2 else 0
    score["防守"] = 2 if stats["avg_conceded"] < 1.0 else 1 if stats["avg_conceded"] < 1.5 else 0
    score["状态"] = 2 if stats["form"].count("W") >= 3 else 1
    score["主/客场"] = stats.get("home_strength", 1)
    score["阵容完整性"] = 2 if stats.get("injuries", "none") == "none" else 1
    return score

def predict_result(score1, score2, t1, t2):
    diff = abs(score1 - score2)
    if diff > 0.75:
        return f"🎯 推荐：主胜（{t1}）" if score1 > score2 else f"🎯 推荐：客胜（{t2}）"
    elif diff > 0.3:
        return "🔍 推荐：主队不败"
    else:
        return "⚠ 建议：走盘或谨慎投注"

def estimate_score_diff(score1, score2):
    diff = score1 - score2
    if diff >= 1.0:
        return "2‑0 或 3‑1"
    elif diff >= 0.5:
        return "1‑0 或 2‑1"
    elif diff > -0.5:
        return "1‑1"
    elif diff > -1.0:
        return "1‑2 或 0‑1"
    else:
        return "0‑2 或 1‑3"

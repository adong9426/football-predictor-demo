import streamlit as st
import json
from utils import rate_team, weighted_score, predict_result, estimate_score_diff

# 加载模拟球队数据
with open("teams_data.json", "r", encoding="utf-8") as f:
    TEAMS = json.load(f)

st.set_page_config(page_title="足球比赛预测 Demo", layout="centered")
st.title("⚽ 足球比赛预测模型（演示版）")
team1 = st.selectbox("选择主队", list(TEAMS.keys()))
team2 = st.selectbox("选择客队", list(TEAMS.keys()), index=1)

if team1 == team2:
    st.warning("请选两支不同球队")
else:
    scores1 = rate_team(TEAMS[team1])
    scores2 = rate_team(TEAMS[team2])
    score1 = weighted_score(scores1)
    score2 = weighted_score(scores2)

    st.subheader("🔢 得分结果")
    st.write(f"🏠 {team1}：{score1:.2f}")
    st.write(f"🚗 {team2}：{score2:.2f}")

    st.subheader("📊 胜负预测")
    st.success(predict_result(score1, score2, team1, team2))

    st.subheader("🎯 比分预测")
    st.info(f"预估比分范围：{estimate_score_diff(score1, score2)}")

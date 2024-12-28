scores ={"数学":82, "国語": 74, "英語": 60, "理科": 92, "社会":70}
diff_score = scores["理科"]-scores["社会"]
print(f"理科は社会より{diff_score}点高いです")

scores_values = list(scores.values())

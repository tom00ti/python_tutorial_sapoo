scores ={"数学":82, "国語": 74, "英語": 60, "理科": 92, "社会":70}
diff_score = scores["理科"]-scores["社会"]
print(f"理科は社会より{diff_score}点高いです")

scores_values = list(scores.values())
avg_score = sum(scores_values)/len(scores_values)
print(f"全教科の平均点は{avg_score}点です")
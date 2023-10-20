score_list = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0, "P":0.0}
sum_course = 0
sum_score = 0

for i in range(20):
  subject, course, score = input().split()
  if score == "P":
    continue
  sum_course += float(course)
  sum_score += (score_list.get(score) * float(course))
  #sum_score += (score_list[score] * float(course))

print(sum_score/sum_course)
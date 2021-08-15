total_score=0
list_of_score=[]
number_of_student=int(input("Please enter the number of students :"))
for i in range(number_of_student):
    score=float(input("Please enter student grade :"))
    list_of_score.append(score)
    total_score+=score
    average=total_score/number_of_student
print("average scores : ",average," , max of scores : ",max(list_of_score), " , min of scores : ",min(list_of_score))
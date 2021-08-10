def solution(scores):
    answer = []
    
    for i in range(len(scores)):
        max_score, min_score = -1, 105
        max_cnt, min_cnt = 0, 0
        sum_score = 0
        sum_people = len(scores)
        
        for j in range(len(scores)):
            if scores[j][i]>max_score:  max_score = scores[j][i]
            if scores[j][i]<min_score:  min_score = scores[j][i]
    
        for j in range(len(scores)):
            if scores[j][i]==max_score: max_cnt+=1
            if scores[j][i]==min_score: min_cnt+=1
                
        for j in range(len(scores)):    sum_score += scores[j][i]

        if max_score == scores[i][i] and max_cnt==1:
            sum_score -= max_score
            sum_people-=1
        
        elif min_score == scores[i][i] and min_cnt==1:
            sum_score -= min_score
            sum_people-=1
            
        sum_avg = sum_score/sum_people
        
        if sum_avg>=90: answer.append("A")
        elif sum_avg>=80:   answer.append("B")
        elif sum_avg>=70:   answer.append("C")
        elif sum_avg>=50:   answer.append("D")
        else:   answer.append("F")

    return "".join(answer)
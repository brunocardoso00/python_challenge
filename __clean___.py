from os import write


class Candidate:
    def __init__(self, name, course, age, state):
        self.name = name
        self.course = course
        self.age = age
        self.state = state

    def to_string(self):
        print(f"{self.name}\n{self.course}\n{self.age}\n{self.state}\n")

def read_file(fileName):
    file = open(fileName, "r", encoding="utf-8")
    contents = file.readlines()
    file.close()
    return contents

def get_candidates(datas):
    candidates = []
    header = datas[0]

    for data in datas:
        if data == header:
            continue

        candidateArray = data.split(";")
        candidate = Candidate(candidateArray[0], candidateArray[1], candidateArray[2], candidateArray[3])
        candidates.append(candidate)

    return candidates

def average_cnadidates_per_course(candidates):
    total = len(candidates)
    totalDotNet = len(get_candidates_of_course(candidates, "API .NET"))
    totalQA = len(get_candidates_of_course(candidates, "QA"))
    totalIOS = len(get_candidates_of_course(candidates, "iOS"))

    print(f"API .NET: {calcule_avg(totalDotNet,total)}% \nQA: {calcule_avg(totalQA,total)}% \nIOS: {calcule_avg(totalIOS,total)}%")

def calcule_avg(quantity, total):
    return (quantity/total)*100

def average_age(candidates, courseName):
    totalCandidates = len(get_candidates_of_course(candidates, courseName))
    totalAgeCandidates = sum_age_of_candidates_of_course(candidates, courseName)
    avarageAge = totalAgeCandidates/totalCandidates

    print(f"A Média de age dos candidatos do {courseName} é {avarageAge}")

def get_oldest_candidate(candidates,courseName):
    courseCandidates = get_candidates_of_course(candidates, courseName)
    oldest = max(map(lambda candidate: int(candidate.age.split(" ")[0]),courseCandidates))
    print(f"O idade do mais velho no curso de {courseName} é {oldest}")

def get_youngest_candidate(candidates, courseName):
    courseCandidates = get_candidates_of_course(candidates, courseName)
    youngest = min(map(lambda candidate: int(candidate.age.split(" ")[0]),courseCandidates))
    print(f"O idade do mais jovem no curso de {courseName} é {youngest}")

def get_candidates_of_course(candidates, courseName):
    return list(filter(lambda candidate: candidate.course == courseName, candidates))

def sum_age_of_candidates_of_course(candidates, courseName):
    courseCandidates = get_candidates_of_course(candidates, courseName)
    return sum(map(lambda candidate: int(candidate.age.split(" ")[0]),courseCandidates))

def total_states(candidates):
    return len(set(list(map(lambda candidate: candidate.state, candidates))))

def save_order_by_name(candidates):
    candidates.sort()
    file = open("Sorted_AppAcademy_Candidates.csv", "w", encoding="utf-8")
    for candidate in candidates:
        file.writelines(candidate)
    file.close()

datas = read_file("AppAcademy_Candidates.csv")

candidates = get_candidates(datas)

average_cnadidates_per_course(candidates)

average_age(candidates,"QA")

get_oldest_candidate(candidates, "iOS")

get_youngest_candidate(candidates, "API .NET")

totalAgeOfCandidate =  sum_age_of_candidates_of_course(candidates, "API .NET")
print(f"a soma das idades dos candidatos do curso de API .NET é:{totalAgeOfCandidate}")

print(f"{total_states(candidates)}")
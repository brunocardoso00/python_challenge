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
        candidate = Candidate(candidateArray[0], candidateArray[1], int(candidateArray[2].split(" ")[0]), candidateArray[3].replace("\n", ""))
        candidates.append(candidate)

    return candidates


def average_cnadidates_per_course(candidates):
    total = len(candidates)
    totalDotNet = len(get_candidates_of_course(candidates, "API .NET"))
    totalQA = len(get_candidates_of_course(candidates, "QA"))
    totalIOS = len(get_candidates_of_course(candidates, "iOS"))

    print(f"API .NET: {calculate_percentage(totalDotNet,total)}% \nQA: {calculate_percentage(totalQA,total)}% \nIOS: {calculate_percentage(totalIOS,total)}%")


def calculate_percentage(quantity, total):
    return (quantity/total)*100


def average_age(candidates, courseName):
    totalCandidates = len(get_candidates_of_course(candidates, courseName))
    totalAgeCandidates = sum_age_of_candidates_of_course(candidates, courseName)
    avarageAge = totalAgeCandidates/totalCandidates

    print(f"A idade media dos candidatos do {courseName} eh de {avarageAge}")


def get_oldest_candidate(candidates, courseName):
    courseCandidates = get_candidates_of_course(candidates, courseName)
    oldest = max(map(lambda candidate: candidate.age, courseCandidates))

    print(f"A idade do mais velho no curso de {courseName} eh {oldest}")


def get_youngest_candidate(candidates, courseName):
    courseCandidates = get_candidates_of_course(candidates, courseName)
    youngest = min(map(lambda candidate: candidate.age, courseCandidates))
    
    print(f"A idade do mais jovem no curso de {courseName} eh {youngest}")


def get_candidates_of_course(candidates, courseName):
    return list(filter(lambda candidate: candidate.course == courseName, candidates))


def sum_age_of_candidates_of_course(candidates, courseName):
    courseCandidates = get_candidates_of_course(candidates, courseName)
    return sum(map(lambda candidate: candidate.age, courseCandidates))


def total_states(candidates):
    return len(set(list(map(lambda candidate: candidate.state, candidates))))


def save_order_by_name(candidates):
    candidates.sort()
    file = open("Sorted_AppAcademy_Candidates.csv", "w", encoding="utf-8")
    for candidate in candidates:
        file.writelines(candidate)
    file.close()

# [x] o instrutor de iOS tem mais de 20 anos
# [] o instrutor de API .NET é mais novo do que o instrutor do iOS
# [x]a idade do instrutor de iOS é um número primo
# [x]o primeiro nome do instrutor de API .NET tem 3 vogais
# [x]a última letra do último nome do instrutor de API .NET é a letra "k"
# [x]a primeira letra do último nome do instrutor de iOS é a letra "V"
# [x]a idade dos instrutores é um número ímpar
# [x]os instrutores nasceram na mesma década
# [x]os instrutores tem menos de 31 anos
# [x]a vaga atribuída aos instrutores (na planilha) não é a vaga na qual eles vão instruir
# [x]os instrutores são de SC
def find_instructors(candidates):

    instructoresCommunRules = list(filter(lambda candidate:
                                          (candidate.age < 31) and
                                          (candidate.age % 2 == 1) and
                                          candidate.state == "SC", candidates))

    ios = list(filter(lambda candidate: candidate.name.split(" ")[1][0] == "V" and
                      candidate.age > 20 and
                      candidate.course != "iOS" and
                      is_prime(candidate.age), instructoresCommunRules))[0]

    apiDotNet = list(filter(lambda candidate:
                            count_vowels(candidate.name.split(" ")[0]) == 3 and
                            candidate.course != "API .NET" and
                            candidate.name.split(" ")[1][-1] == "k" and
                            (ios.age - candidate.age) <= 10, instructoresCommunRules))[0]

    print("O instrutor do iOS eh: " + ios.name)
    print("O instrutor de apiDotNet eh: " + apiDotNet.name)

def is_prime(value):
    if value > 1:
        for i in range(2, value + 1):
            if value % i == 0 and i != value and i != 1:
                return False
            else:
                return True
    else:
        return False


def count_vowels(string):
    vowel = "aieou"
    quantity = 0
    string = string.lower()
    for char in string:
        if char in vowel:
            quantity = quantity + 1
    return quantity


datas = read_file("AppAcademy_Candidates.csv")

candidates = get_candidates(datas)

average_cnadidates_per_course(candidates)

average_age(candidates, "QA")

get_oldest_candidate(candidates, "iOS")

get_youngest_candidate(candidates, "API .NET")

totalAgeOfCandidate = sum_age_of_candidates_of_course(candidates, "API .NET")

print(f"A soma das idades dos candidatos de API .NET eh igual a:{totalAgeOfCandidate}")

print(f"A quantidade de estados distintos sao de:{total_states(candidates)} estados")

find_instructors(candidates)

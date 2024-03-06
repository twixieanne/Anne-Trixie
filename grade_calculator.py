def grade_calculator(score):

    if score >= 90:
      return "A"
    elif score >= 80:
      return "B"
    elif score >= 70:
      return "C"
    elif score >= 60:
      return "D"
    else:
      return "F"

def calculate_weighted_average(grades, weights):

  if len(grades) != len(weights):
    raise ValueError("Number of grades and weights must be equal.")

  weighted_sum = sum(grade * weight for grade, weight in zip(grades, weights))
  total_weight = sum(weights)

  return weighted_sum / total_weight

def calculate_average(grades):

  return sum(grades) / len(grades)

def main():

  while True:
    try:
      grades_str = input("Enter your 5 grades separated by commas (or -1 to quit): ")
      if grades_str == "-1":
        break

      grades = [int(grade.strip()) for grade in grades_str.split(",")]

      weights_str = input("Enter the corresponding weights for each grade separated by commas (or leave blank for simple average): ")
      if weights_str:
        weights = [float(weight.strip()) for weight in weights_str.split(",")]

        if len(weights_str.split(",")) != len(grades):
          raise ValueError("Number of grades and weights must match.")
        if not all(weight >= 0 for weight in weights):
          raise ValueError("Weights must be non-negative.")
      else:
        weights = None

      if not all(0 <= score <= 100 for score in grades):
        raise ValueError("Grades must be between 0 and 100.")

      for score, weight in zip(grades, weights or grades):
        letter_grade = grade_calculator(score)
        print(f"{score} = {letter_grade}")

      if weights:
        weighted_average = calculate_weighted_average(grades, weights)
        print(f"Weighted Average: {weighted_average:.2f}")

      average = calculate_average(grades)
      print(f"Average: {average:.2f}")

    except ValueError as e:
      print(f"Invalid input: {e}")

main()

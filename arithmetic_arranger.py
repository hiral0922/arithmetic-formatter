def arithmetic_arranger(problems, answer_flag=False):
  
  if len(problems) > 5:
    return "Error: Too many problems."

  operand1_array = []
  operand2_array = []
  dash_array = []
  answer_array = []
  
  for expression in problems:
    expression_split = expression.split()
    operand1 = expression_split[0]
    operator = expression_split[1]
    operand2 = expression_split[2]
    
    if len(operand1) <= 4 and len(operand2) <= 4:
      if operand1.isdigit() and operand2.isdigit():
        if operator == "+" or operator == "-":
          pass
        else:
          return "Error: Operator must be '+' or '-'."
      else:
        return "Error: Numbers must only contain digits."
    else:
      return "Error: Numbers cannot be more than four digits."
      
    len_of_dash = 0
    
    if len(operand1) > len(operand2):
      len_of_dash = len(operand1) + 2
    elif len(operand2) > len(operand1):
      len_of_dash = len(operand2) + 2
    else:
      len_of_dash = len(operand1) + 2

    right_aligned_operand1 = operand1.rjust(len_of_dash)
    right_aligned_operand2 = operand2.rjust(len_of_dash-2)
    left_aligned_operator = operator.ljust(0)
    operator_and_operand2 = left_aligned_operator + " " + right_aligned_operand2
    
    operand1_array.append(right_aligned_operand1)
    operand2_array.append(operator_and_operand2)
    
    dash_together = "-" * len_of_dash
    dash_array.append(dash_together)

    if operator == "+":
      answer = int(operand1) + int(operand2)
    else:
      answer = int(operand1) - int(operand2)
      
    answer = str(answer)
    answer = answer.rjust(len_of_dash)
    answer_array.append(answer)

  if answer_flag == True:
    arranged_problem = "    ".join(operand1_array) + "\n" + "    ".join(operand2_array) + "\n" + "    ".join(dash_array) + "\n" + "    ".join(answer_array)
  else:
    arranged_problem = "    ".join(operand1_array) + "\n" + "    ".join(operand2_array) + "\n" + "    ".join(dash_array)
    

  return arranged_problem
      
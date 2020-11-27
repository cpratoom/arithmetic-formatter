def arithmetic_arranger(problems, compute=False):
    top = ""
    bot = ""
    sep = ""
    ans = ""

    if len(problems) > 5:
        errmsg = "Error: Too many problems."
        return errmsg
    else:
        for problem in problems:
            one, op, two = problem.split()
            
            if not (one.isnumeric() and two.isnumeric()):
                errmsg = "Error: Numbers must only contain digits."
                return errmsg
            elif not (op=='+' or op=='-'):
                errmsg = "Error: Operator must be '+' or '-'." 
                return errmsg
            else:
                if len(one)>4 or len(two)>4:
                    errmsg = "Error: Numbers cannot be more than four digits."
                    return errmsg
                else: 
                    
                    fac = (1 if op=='+' else -1)
                    width = 2+ max(len(one), len(two))
                    
                    if problem==problems[-1]:
                        trail = ""
                    else:
                        trail = " "*4
                        
                    top += one.rjust(width, ' ') + trail
                    bot += op.ljust(width-len(two),' ') + two + trail
                    sep += ''.rjust(width, '-') + trail
                    ans += str( int(one) + fac*int(two) ).rjust(width, ' ') + trail
                    
                    if compute:
                        arranged_problems = \
                        top + "\n" + \
                        bot + "\n" + \
                        sep + "\n" + \
                        ans
                    else:
                        arranged_problems = \
                        top + "\n" + \
                        bot + "\n" + \
                        sep
    

    return arranged_problems
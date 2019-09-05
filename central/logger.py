class Logger(object):

    def __init__(self,
                 pnum,
                 company,
                 category,
                 level):

        self.pnum = pnum
        self.company = company
        self.category = category
        self.level = level

    def flushvars(self, vars_to_interpret, num_iters, return_val):

        strtoflush = "\n[Logger] -=- [INTERPRET]\n\n"
        strtoflush += "P#{} => asked by {} (categorized by me as {}) with difficulty {}\n".format(
            self.pnum, self.company, self.category, self.level
        )
        for it in range(num_iters):
            for k, v in vars_to_interpret.items():
                strtoflush += "[Iteration {}] {} => {}\n".format(it+1, k, v[it])
            strtoflush += "-======================================================-\n"

        strtoflush += "Return Value: {}\n".format(str(return_val))

        print(strtoflush)

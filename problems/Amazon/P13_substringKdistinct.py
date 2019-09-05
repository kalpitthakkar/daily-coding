from central import Solver

class Problem13(Solver):

    def __init__(self,
                 pnum,
                 desc,
                 company,
                 category,
                 level,
                 logging=True):

        super(Problem13, self).__init__(
            pnum, desc, company, category, level,
            logging
        )

    def solve(self, x, **kwargs):
        k = kwargs['k']
        NUM_CHARS = 26

        def checkAtMostK(freq_map, k):
            num_distinct = 0
            for i in range(NUM_CHARS):
                if freq_map[i] > 0:
                    num_distinct += 1

            return (num_distinct <= k)

        start = 0
        end = 0
        char_count = [0] * NUM_CHARS
        substr = x[0]
        maxlen = 1
        char_count[ord(x[0]) - ord('a')] += 1
        end += 1
        while(end < len(x)):
            char_count[ord(x[end]) - ord('a')] += 1
            feasible = checkAtMostK(char_count, k)
            while(not feasible):
                char_count[ord(x[start]) - ord('a')] -= 1
                start += 1
                feasible = checkAtMostK(char_count, k)
            end += 1
            curr_len = (end - start)
            if curr_len > maxlen:
                substr = x[start:end]
                maxlen = curr_len

        return substr

    def interpret(self, x, **kwargs):
        return

if __name__ == '__main__':
    desc = ("Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.\n\n" +
            "For example, given s = \"abcba\" and k = 2, the longest substring with k distinct characters is \"bcb\".\n\n")
    p = Problem13(
        pnum=13,
        desc=desc,
        company="Amazon",
        category="String manipulation",
        level="Hard",
        logging=False
    )
    p.print_description()

    x = input("Enter the string : ")
    k = input("Enter the value of K: ")
    k = int(k)

    solver = p._get_solver()

    print("Solution for the given input: {}".format(solver(x, k=k)))
    if p.logging:
        interpreter = p._get_interpreter()
        interpreter(x, k=k)

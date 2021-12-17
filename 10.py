from util.util import file_to_string_list
import sys

OPEN_SET = set(["{", "[", "(", "<"])
CLOSE_SET = set(["}", "]", ")", ">"])
MATCH = {"{":"}", "[":"]", "(":")", "<":">"}
SCORE = {"}": 1197, ">": 25137, "]": 57, ")":3}
AUTOCOMPLETE_SCORE = {"(": 1, "[":2, "{":3, "<":4}

def compute_syntax_error(filename):
    chunks = file_to_string_list(filename)
    error_score = 0
    for chunk in chunks:
        stack = []
        for i in range(len(chunk)):
            if chunk[i] in OPEN_SET:
                stack.append(chunk[i])
            if chunk[i] in CLOSE_SET:
                popped = stack.pop()
                if MATCH[popped] != chunk[i]:
                    error_score += SCORE[chunk[i]]
    return error_score

def compute_completion_score(filename):
    chunks = file_to_string_list(filename)
    scores = []
    for chunk in chunks:
        stack = []
        ignore = False
        for i in range(len(chunk)):
            if chunk[i] in OPEN_SET:
                stack.append(chunk[i])
            if chunk[i] in CLOSE_SET:
                popped = stack.pop()
                if MATCH[popped] != chunk[i]:
                    ignore = True
        if not ignore:
            score = 0
            for _ in range(len(stack)):
                popped = stack.pop()
                score = score * 5 + AUTOCOMPLETE_SCORE[popped]
            scores.append(score)
    scores = sorted(scores)
    return scores[len(scores) // 2]


def main():
    print(compute_syntax_error(sys.argv[1]))
    print(compute_completion_score(sys.argv[1]))

main()

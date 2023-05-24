from collections import deque
box = 50
eggs = deque([int(x) for x in input().split(", ")])
papers = deque([int(x) for x in input().split(", ")])
box_counter = 0

while eggs and papers:
    test_egg = eggs[0]
    test_paper = papers[-1]
    if test_egg <= 0:
        eggs.popleft()
    elif test_egg == 13:
        eggs.popleft()
        l_el = papers.popleft()
        r_el = papers.pop()
        papers.appendleft(r_el)
        papers.append(l_el)
    elif test_egg + test_paper > box:
        eggs.popleft()
        papers.pop()
    else:
        eggs.popleft()
        papers.pop()
        box_counter += 1
if box_counter:
    print(f"Great! You filled {box_counter} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join(str(x) for x in eggs)}')
if papers:
    print(f'Pieces of paper left: {", ".join(str(x) for x in papers)}')

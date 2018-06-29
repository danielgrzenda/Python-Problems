import sys

if __name__ == "__main__":
    first, second = [int(x) for x in sys.stdin.readlines()]
    ans = (((second-first)-180)%360)-180
    if ans == -180:
        print(180)
    else:
        print(ans)
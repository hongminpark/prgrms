# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frames):
    global N
    N = n
    built_frames = set()
    for frame in build_frames:
        if available(frame, built_frames):
            if frame[3]:
                built_frames.add((frame[0], frame[1], frame[2]))
            else:
                built_frames.remove((frame[0], frame[1], frame[2]))

    built_frames = [[x, y, z] for x, y, z in built_frames]
    built_frames.sort(key=lambda x: (x[0], x[1], x[2]))
    return built_frames

def available(frame, built_frames):
    x, y, a, b = frame[0], frame[1], frame[2], frame[3]
    if b:
        if a:
            if ((x, y-1, 0) in built_frames or (x+1, y-1, 0) in built_frames) or \
             ((x - 1, y, 1) in built_frames and (x + 1, y, 1) in built_frames):
                return True
        else:
            if y == 0 or (x - 1, y, 1) in built_frames or (x, y, 1) in built_frames or (x, y - 1, 0) in built_frames:
                return True
        return False

    else:
        tmp_frames = built_frames - {(x, y, a)}
        if a:
            nexts = [(x-1, y, 1), (x+1, y, 1), (x-1, y, 1), (x+1, y, 0)]
        else:
            nexts = [(x-1, y+1, 1), (x, y+1, 1), (x, y+1, 0)]

        for x, y, a in nexts:
            if (x, y, a) in tmp_frames and not available((x, y, a, 1), tmp_frames - {(x, y, a)}):
                return False
        return True

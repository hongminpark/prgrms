# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frames):
    frames = set()
    for x, y, a, b in build_frames:
        if b == 1:
            if available(x, y, a, frames):
                frames.add((x, y, a))
        else:
            if a == 0:
                if available(x, y + 1, 0, frames) and available(x - 1, y + 1, 1, frames) and available(x, y + 1, 1, frames):
                    frames -= {(x, y, a)}
            else:
                frames_ = frames - {(x, y, a)}
                if available(x - 1, y, 1, frames_) and available(x + 1, y, 1, frames_) \
                        and available(x, y, 0, frames_) and available(x + 1, y, 0, frames_):
                    frames = frames_
    frames = [[x, y, z] for x, y, z in frames]
    frames.sort(key=lambda x: (x[0], x[1], x[2]))
    return frames


def available(x, y, a, frames):
    if y == 0:
        return True

    if a == 0:
        if (x - 1, y, 1) in frames or (x, y, 1) in frames or (x, y - 1, 0) in frames:
            return True
    else:
        if ((x, y - 1, 0) in frames or (x + 1, y - 1, 0) in frames) or \
                ((x - 1, y, 1) in frames and (x + 1, y, 1) in frames):
            return True

    return False

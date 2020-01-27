def solution(record):
    keep = list()
    store = list()

    for r in record:
        if r[0:4] == 'SAVE':
            if not keep:
                continue
            store.extend(keep)
            keep = []
        elif r[0:7] == 'DELETE':
            if not keep:
                continue
            keep.pop()
        else:
            email = r.split(' ')[1]
            keep.append(email)

    print(store)
    return store

solution(["RECEIVE abcd@naver.com", "RECEIVE zzkn@naver.com", "DELETE", "RECEIVE qwerty@naver.com", "SAVE", "SAVE", "DELETE", "RECEIVE QwerTY@naver.com", "SAVE"])
from collections import defaultdict
import re


def solution(word, pages):
    page_dict = {}
    linked_dict = defaultdict(list)

    for idx, page in enumerate(pages):
        meta = re.search('<meta(.+?)/>', page).group()
        my_link = re.search('"http.+"', meta).group()
        out_links = re.findall('<a(.+?)>', page)
        out_links = [re.search('"http.+"', link).group() for link in out_links]
        word_count = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())

        page_dict[my_link] = {'index': idx, 'score': word_count, 'out_link_count': len(out_links)}

        for out_link in out_links:
            linked_dict[out_link].append(my_link)

    match_scores = []
    for my_link in page_dict:
        match_score = page_dict[my_link]['score']

        for linked_link in linked_dict[my_link]:
            if page_dict[linked_link]['out_link_count'] == 0:
                continue
            match_score += page_dict[linked_link]['score'] / page_dict[linked_link]['out_link_count']

        match_scores.append((match_score, page_dict[my_link]['index']))

    return sorted(match_scores, key=lambda x: (-x[0], x[1]))[0][1]


print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
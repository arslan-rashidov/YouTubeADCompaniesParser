from urllib.parse import urlparse

import requests, re
from urllib.request import Request, urlopen
import scrapetube

import matplotlib.pyplot as plt


def get_description(video_url):
    resp = requests.get(video_url).text
    desc = re.findall(r'"shortDescription":".*?",', resp)[0][20:-2]
    return desc


def get_links_from_description(desc):
    link_pattern = r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
    links_re = re.findall(link_pattern, desc)
    links = []

    for link_re in links_re:
        link = link_re[0] + "://" + link_re[1] + link_re[2]
        links.append(link)

    return links


def get_last_link_from_link_redirections(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        finalURL = urlopen(req).geturl()
        print(finalURL)
        return finalURL
    except:
        print("ERROR")
        return Exception


def get_channel_videos_urls(channel_url):
    videos = scrapetube.get_channel(channel_url=channel_url)
    videos_urls = []
    for video in videos:
        videos_urls.append("https://www.youtube.com/watch?v=" + str(video['videoId']))
    return videos_urls


def get_domain_names(links):
    domain_names = []

    for link in links:
        domain_name = urlparse(link).netloc
        if 'www.' in domain_name:
            domain_name = domain_name[4:]
        domain_names.append(domain_name)

    return domain_names


def count_domain_names(domain_names):
    domain_names_count = {}
    for domain_name in domain_names:
        if domain_name in domain_names_count.keys():
            domain_names_count[domain_name] += 1
        else:
            domain_names_count[domain_name] = 1
    return domain_names_count


def print_domain_names_count(domain_names_count):
    domain_names = list(domain_names_count.keys())
    for i in range(len(domain_names_count.keys())):
        domain_name = domain_names[i]
        domain_name_count = domain_names_count[domain_name]
        print(f"{i + 1}. {domain_name} - {domain_name_count}")


def show_bar(domain_names_count):
    y = list(domain_names_count.keys())

    # getting values against each value of y
    x = list(domain_names_count.values())
    plt.barh(y, x)

    # setting label of y-axis
    plt.ylabel("Domain Names")

    # setting label of x-axis
    plt.xlabel("Domain Names Count")
    plt.title("VDud Advertisment Company Analize")

    plt.show()


def main():
    channel_url = "https://www.youtube.com/c/SlivkiChanel/videos"
    videos_urls = get_channel_videos_urls(channel_url)
    print(videos_urls)

    descriptions = []
    desc_count = 0
    for video_url in videos_urls:
        desc_count += 1
        description = get_description(video_url)
        descriptions.append(description)
        print(f"Description got for {desc_count}/{len(videos_urls)}")

    unredirected_links_in_videos = []
    unredir_count = 0
    for description in descriptions:
        unredir_count += 1
        unredirected_links_in_video = get_links_from_description(description)
        for unredirected_link_in_video in unredirected_links_in_video:
            unredirected_links_in_videos.append(unredirected_link_in_video)
        print(f"Unredirected links got for descriptions {unredir_count}/{len(descriptions)}")

    redirected_links_in_videos = []
    redir_count = 0
    for unredirected_link_in_video in unredirected_links_in_videos:
        redir_count += 1
        redirected_link = get_last_link_from_link_redirections(unredirected_link_in_video)
        if redirected_link != Exception:
            redirected_links_in_videos.append(redirected_link)
        print(f"Redirected links got for unredirected links {redir_count}/{len(unredirected_links_in_videos)} ()")

    domain_names = get_domain_names(redirected_links_in_videos)
    domain_names_count = count_domain_names(domain_names)
    domain_names_count = {k: v for k, v in sorted(domain_names_count.items(), key=lambda item: item[1])}

    delete_indexes = None
    while delete_indexes != []:
        print_domain_names_count(domain_names_count)
        delete_indexes = input("\nВведите индексы доменов, которые хотите удалить или нажмите ENTER:").split()
        if delete_indexes == []:
            break
        delete_domain_names = []
        domain_names = list(domain_names_count.keys())
        for i in range(len(delete_indexes)):
            delete_domain_names.append(domain_names[int(delete_indexes[i]) - 1])
        for domain_name in delete_domain_names:
            del (domain_names_count[domain_name])

    print(domain_names_count)
    show_bar(domain_names_count)


main()

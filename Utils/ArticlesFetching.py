import feedparser as fp


def fetch_articles(rss_dict: dict):
    result_dict = {}
    for dict_entry in rss_dict.items():
        result_dict[dict_entry[0]] = get_title_and_links_list(dict_entry[1])
    return result_dict


def get_title_and_links_list(url: str):
    result_list = []
    try:
        news_feed = fp.parse(url)
    except:
        return result_list

    for i in range(min(10, len(news_feed.entries))):
        entry = news_feed.entries[i]
        temp_list = []
        try:
            temp_list.append(entry.title)
        except:
            pass
        try:
            temp_list.append(entry.link)
        except:
            pass
        try:
            temp_list.append(entry.published)
        except:
            pass
        if len(temp_list) != 0:
            result_list.append(temp_list)
    return result_list

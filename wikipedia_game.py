import wikipedia
import sys
import os


arguments = sys.argv
print(arguments[1])

def wiki():
    print('\n\n\t\t===== Wikipedia Game =====\n\n')
    srcpg = get(arguments[1])
    targetpg = get(arguments[2])
    List = {}
    List[srcpg.title] = {
        'title': srcpg.title,
        'parent': None
    }
    LL = [List[srcpg.title]]
    while LL:
        current = LL[0]
        LL = LL[1:]
        try:
            temp = wikipedia.page(current['title'])
            print('\t%s' % temp.title)
            for link in temp.links:
                if link not in List:
                    List[link] = {
                        'title': link,
                        'parent': current
                    }
                    if link == targetpg.title:
                        print('\n%s found!' % link)
                        print('Path: ', end='')
                        path(List[link])
                        print()
                        sys.exit()
                    LL.append(List[link])

        except KeyboardInterrupt:
            print('End Game!')
            sys.exit()

        except wikipedia.exceptions.DisambiguationError as e:
            # Disambiguation Page
            List[e.title] = {
                'title': e.title,
                'parent': current
            }
        #    Adds every link on disambiguation page to queue
            for option in e.options:
                if option not in List:
                    List[option] = {
                        'title': option,
                        'parent': List[e.title]
                    }
                    if option == targetpg.title:
                        print('\nTarget %s found!' % option)
                        print('Path found is : ', end='')
                        path(List[option])
                        print()
                        sys.exit()
                    LL.append(List[option])

def get(Source):
    page = None
    while not page:
        try:
            #src = input('Please enter the %s :' % Source)
            src = Source
            page = wikipedia.page(src)
        except wikipedia.exceptions.PageError as e:
            print('Error.. End Game!')
        except KeyboardInterrupt:
            print('End Game!')
            sys.exit()
        except wikipedia.exceptions.DisambiguationError as e:
            print('\nDisambiguation Selection (Choose one of these or use another term)')
            for option in e.options:
                print('\t' + option)
    return page

def path(tr_l):
    if tr_l['parent']:
        path(tr_l['parent'])
        print(' -> ', end='')
    print(tr_l['title'], end='')


wiki()

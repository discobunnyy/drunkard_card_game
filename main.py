import cv2

similar = []
similar2 = []

img_1 = cv2.imread('cards/8_spade.png', 0)
img_2 = cv2.imread('cards/king_heart.png', 0)

img_ace_heart = cv2.imread('cards/ace_heart.png', 0)
img_king_heart = cv2.imread('cards/king_heart.png', 0)
img_queen_heart = cv2.imread('cards/queen_heart.png', 0)
img_jack_heart = cv2.imread('cards/jack_heart.png', 0)
img_10_heart = cv2.imread('cards/10_heart.png', 0)
img_9_heart = cv2.imread('cards/9_heart.png', 0)
img_8_heart = cv2.imread('cards/8_heart.png', 0)
img_7_heart = cv2.imread('cards/7_heart.png', 0)
img_6_heart = cv2.imread('cards/6_heart.png', 0)

img_ace_spade = cv2.imread('cards/ace_spade.png', 0)
img_king_spade = cv2.imread('cards/king_spade.png', 0)
img_queen_spade = cv2.imread('cards/queen_spade.png', 0)
img_jack_spade = cv2.imread('cards/jack_spade.png', 0)
img_10_spade = cv2.imread('cards/10_spade.png', 0)
img_9_spade = cv2.imread('cards/9_spade.png', 0)
img_8_spade = cv2.imread('cards/8_spade.png', 0)
img_7_spade = cv2.imread('cards/7_spade.png', 0)
img_6_spade = cv2.imread('cards/6_spade.png', 0)

img_ace_diamond = cv2.imread('cards/ace_diamond.png', 0)
img_king_diamond = cv2.imread('cards/king_diamond.png', 0)
img_queen_diamond = cv2.imread('cards/queen_diamond.png', 0)
img_jack_diamond = cv2.imread('cards/jack_diamond.png', 0)
img_10_diamond = cv2.imread('cards/10_diamond.png', 0)
img_9_diamond = cv2.imread('cards/9_diamond.png', 0)
img_8_diamond = cv2.imread('cards/8_diamond.png', 0)
img_7_diamond = cv2.imread('cards/7_diamond.png', 0)
img_6_diamond = cv2.imread('cards/6_diamond.png', 0)

img_ace_club = cv2.imread('cards/ace_club.png', 0)
img_king_club = cv2.imread('cards/king_club.png', 0)
img_queen_club = cv2.imread('cards/queen_club.png', 0)
img_jack_club = cv2.imread('cards/jack_club.png', 0)
img_10_club = cv2.imread('cards/10_club.png', 0)
img_9_club = cv2.imread('cards/9_club.png', 0)
img_8_club = cv2.imread('cards/8_club.png', 0)
img_7_club = cv2.imread('cards/7_club.png', 0)
img_6_club = cv2.imread('cards/6_club.png', 0)

#------------------------------------------------
orb = cv2.ORB_create()
#------------------------------------------------

kp_1, des_1 = orb.detectAndCompute(img_1, None)
kp_ace_heart, des_ace_heart = orb.detectAndCompute(img_ace_heart, None)
kp_king_heart, des_king_heart = orb.detectAndCompute(img_king_heart, None)
kp_queen_heart, des_queen_heart = orb.detectAndCompute(img_queen_heart, None)
kp_jack_heart, des_jack_heart = orb.detectAndCompute(img_jack_heart, None)
kp_10_heart, des_10_heart = orb.detectAndCompute(img_10_heart, None)
kp_9_heart, des_9_heart = orb.detectAndCompute(img_9_heart, None)
kp_8_heart, des_8_heart = orb.detectAndCompute(img_8_heart, None)
kp_7_heart, des_7_heart = orb.detectAndCompute(img_7_heart, None)
kp_6_heart, des_6_heart = orb.detectAndCompute(img_6_heart, None)

kp_ace_spade, des_ace_spade = orb.detectAndCompute(img_ace_spade, None)
kp_king_spade, des_king_spade = orb.detectAndCompute(img_king_spade, None)
kp_queen_spade, des_queen_spade = orb.detectAndCompute(img_queen_spade, None)
kp_jack_spade, des_jack_spade = orb.detectAndCompute(img_jack_spade, None)
kp_10_spade, des_10_spade = orb.detectAndCompute(img_10_spade, None)
kp_9_spade, des_9_spade = orb.detectAndCompute(img_9_spade, None)
kp_8_spade, des_8_spade = orb.detectAndCompute(img_8_spade, None)
kp_7_spade, des_7_spade = orb.detectAndCompute(img_7_spade, None)
kp_6_spade, des_6_spade = orb.detectAndCompute(img_6_spade, None)


kp_ace_diamond, des_ace_diamond = orb.detectAndCompute(img_ace_diamond, None)
kp_king_diamond, des_king_diamond = orb.detectAndCompute(img_king_diamond, None)
kp_queen_diamond, des_queen_diamond = orb.detectAndCompute(img_queen_diamond, None)
kp_jack_diamond, des_jack_diamond = orb.detectAndCompute(img_jack_diamond, None)
kp_10_diamond, des_10_diamond = orb.detectAndCompute(img_10_diamond, None)
kp_9_diamond, des_9_diamond = orb.detectAndCompute(img_9_diamond, None)
kp_8_diamond, des_8_diamond = orb.detectAndCompute(img_8_diamond, None)
kp_7_diamond, des_7_diamond = orb.detectAndCompute(img_7_diamond, None)
kp_6_diamond, des_6_diamond = orb.detectAndCompute(img_6_diamond, None)


kp_ace_club, des_ace_club = orb.detectAndCompute(img_ace_club, None)
kp_king_club, des_king_club = orb.detectAndCompute(img_king_club, None)
kp_queen_club, des_queen_club = orb.detectAndCompute(img_queen_club, None)
kp_jack_club, des_jack_club = orb.detectAndCompute(img_jack_club, None)
kp_10_club, des_10_club = orb.detectAndCompute(img_10_club, None)
kp_9_club, des_9_club = orb.detectAndCompute(img_9_club, None)
kp_8_club, des_8_club = orb.detectAndCompute(img_8_club, None)
kp_7_club, des_7_club = orb.detectAndCompute(img_7_club, None)
kp_6_club, des_6_club = orb.detectAndCompute(img_6_club, None)

#------------------------------------------------

bf = cv2.BFMatcher()
matches_ace_heart = bf.knnMatch(des_1, des_ace_heart, k=2)
matches_king_heart = bf.knnMatch(des_1, des_king_heart, k=2)
matches_queen_heart = bf.knnMatch(des_1, des_queen_heart, k=2)
matches_jack_heart = bf.knnMatch(des_1, des_jack_heart, k=2)
matches_10_heart = bf.knnMatch(des_1, des_10_heart, k=2)
matches_9_heart = bf.knnMatch(des_1, des_9_heart, k=2)
matches_8_heart = bf.knnMatch(des_1, des_8_heart, k=2)
matches_7_heart = bf.knnMatch(des_1, des_7_heart, k=2)
matches_6_heart = bf.knnMatch(des_1, des_6_heart, k=2)


matches_ace_spade = bf.knnMatch(des_1, des_ace_spade, k=2)
matches_king_spade = bf.knnMatch(des_1, des_king_spade, k=2)
matches_queen_spade = bf.knnMatch(des_1, des_queen_spade, k=2)
matches_jack_spade = bf.knnMatch(des_1, des_jack_spade, k=2)
matches_10_spade = bf.knnMatch(des_1, des_10_spade, k=2)
matches_9_spade = bf.knnMatch(des_1, des_9_spade, k=2)
matches_8_spade = bf.knnMatch(des_1, des_8_spade, k=2)
matches_7_spade = bf.knnMatch(des_1, des_7_spade, k=2)
matches_6_spade = bf.knnMatch(des_1, des_6_spade, k=2)


matches_ace_diamond = bf.knnMatch(des_1, des_ace_diamond, k=2)
matches_king_diamond = bf.knnMatch(des_1, des_king_diamond, k=2)
matches_queen_diamond = bf.knnMatch(des_1, des_queen_diamond, k=2)
matches_jack_diamond = bf.knnMatch(des_1, des_jack_diamond, k=2)
matches_10_diamond = bf.knnMatch(des_1, des_10_diamond, k=2)
matches_9_diamond = bf.knnMatch(des_1, des_9_diamond, k=2)
matches_8_diamond = bf.knnMatch(des_1, des_8_diamond, k=2)
matches_7_diamond = bf.knnMatch(des_1, des_7_diamond, k=2)
matches_6_diamond = bf.knnMatch(des_1, des_6_diamond, k=2)


matches_ace_club = bf.knnMatch(des_1, des_ace_club, k=2)
matches_king_club = bf.knnMatch(des_1, des_king_club, k=2)
matches_queen_club = bf.knnMatch(des_1, des_queen_club, k=2)
matches_jack_club = bf.knnMatch(des_1, des_jack_club, k=2)
matches_10_club = bf.knnMatch(des_1, des_10_club, k=2)
matches_9_club = bf.knnMatch(des_1, des_9_club, k=2)
matches_8_club = bf.knnMatch(des_1, des_8_club, k=2)
matches_7_club = bf.knnMatch(des_1, des_7_club, k=2)
matches_6_club = bf.knnMatch(des_1, des_6_club, k=2)

#------------------------------------------------------

good_ace_heart = []
for m, n in matches_ace_heart:
    if m.distance < 0.8*n.distance:
        good_ace_heart.append([m])
similar.append((len(good_ace_heart)))

good_king_heart = []
for m, n in matches_king_heart:
    if m.distance < 0.8*n.distance:
        good_king_heart.append([m])
similar.append((len(good_king_heart)))

good_queen_heart = []
for m, n in matches_queen_heart:
    if m.distance < 0.8*n.distance:
        good_queen_heart.append([m])
similar.append((len(good_queen_heart)))

good_jack_heart = []
for m, n in matches_jack_heart:
    if m.distance < 0.8*n.distance:
        good_jack_heart.append([m])
similar.append((len(good_jack_heart)))

good_10_heart = []
for m, n in matches_10_heart:
    if m.distance < 0.8*n.distance:
        good_10_heart.append([m])
similar.append((len(good_10_heart)))

good_9_heart = []
for m, n in matches_9_heart:
    if m.distance < 0.8*n.distance:
        good_9_heart.append([m])
similar.append((len(good_9_heart)))

good_8_heart = []
for m, n in matches_8_heart:
    if m.distance < 0.8*n.distance:
        good_8_heart.append([m])
similar.append((len(good_8_heart)))

good_7_heart = []
for m, n in matches_7_heart:
    if m.distance < 0.8*n.distance:
        good_7_heart.append([m])
similar.append((len(good_7_heart)))

good_6_heart = []
for m, n in matches_6_heart:
    if m.distance < 0.8*n.distance:
        good_6_heart.append([m])
similar.append((len(good_6_heart)))
#=================================

good_ace_spade = []
for m, n in matches_ace_spade:
    if m.distance < 0.8*n.distance:
        good_ace_spade.append([m])
similar.append((len(good_ace_spade)))

good_king_spade = []
for m, n in matches_king_spade:
    if m.distance < 0.8*n.distance:
        good_king_spade.append([m])
similar.append((len(good_king_spade)))

good_queen_spade = []
for m, n in matches_queen_spade:
    if m.distance < 0.8*n.distance:
        good_queen_spade.append([m])
similar.append((len(good_queen_spade)))

good_jack_spade = []
for m, n in matches_jack_spade:
    if m.distance < 0.8*n.distance:
        good_jack_spade.append([m])
similar.append((len(good_jack_spade)))

good_10_spade = []
for m, n in matches_10_spade:
    if m.distance < 0.8*n.distance:
        good_10_spade.append([m])
similar.append((len(good_10_spade)))

good_9_spade = []
for m, n in matches_9_spade:
    if m.distance < 0.8*n.distance:
        good_9_spade.append([m])
similar.append((len(good_9_spade)))

good_8_spade = []
for m, n in matches_8_spade:
    if m.distance < 0.8*n.distance:
        good_8_spade.append([m])
similar.append((len(good_8_spade)))

good_7_spade = []
for m, n in matches_7_spade:
    if m.distance < 0.8*n.distance:
        good_7_spade.append([m])
similar.append((len(good_7_spade)))

good_6_spade = []
for m, n in matches_6_spade:
    if m.distance < 0.8*n.distance:
        good_6_spade.append([m])
similar.append((len(good_6_spade)))
#==================================

good_ace_diamond = []
for m, n in matches_ace_diamond:
    if m.distance < 0.8*n.distance:
        good_ace_diamond.append([m])
similar.append((len(good_ace_diamond)))

good_king_diamond = []
for m, n in matches_king_diamond:
    if m.distance < 0.8*n.distance:
        good_king_diamond.append([m])
similar.append((len(good_king_diamond)))

good_queen_diamond = []
for m, n in matches_queen_diamond:
    if m.distance < 0.8*n.distance:
        good_queen_diamond.append([m])
similar.append((len(good_queen_diamond)))

good_jack_diamond = []
for m, n in matches_jack_diamond:
    if m.distance < 0.8*n.distance:
        good_jack_diamond.append([m])
similar.append((len(good_jack_diamond)))

good_10_diamond = []
for m, n in matches_10_diamond:
    if m.distance < 0.8*n.distance:
        good_10_diamond.append([m])
similar.append((len(good_10_diamond)))

good_9_diamond = []
for m, n in matches_9_diamond:
    if m.distance < 0.8*n.distance:
        good_9_diamond.append([m])
similar.append((len(good_9_diamond)))

good_8_diamond = []
for m, n in matches_8_diamond:
    if m.distance < 0.8*n.distance:
        good_8_diamond.append([m])
similar.append((len(good_8_diamond)))

good_7_diamond = []
for m, n in matches_7_diamond:
    if m.distance < 0.8*n.distance:
        good_7_diamond.append([m])
similar.append((len(good_7_diamond)))

good_6_diamond = []
for m, n in matches_6_diamond:
    if m.distance < 0.8*n.distance:
        good_6_diamond.append([m])
similar.append((len(good_6_diamond)))
#===================================

good_ace_club = []
for m, n in matches_ace_club:
    if m.distance < 0.8*n.distance:
        good_ace_club.append([m])
similar.append((len(good_ace_club)))

good_king_club = []
for m, n in matches_king_club:
    if m.distance < 0.8*n.distance:
        good_king_club.append([m])
similar.append((len(good_king_club)))

good_queen_club = []
for m, n in matches_queen_club:
    if m.distance < 0.8*n.distance:
        good_queen_club.append([m])
similar.append((len(good_queen_club)))

good_jack_club = []
for m, n in matches_jack_club:
    if m.distance < 0.8*n.distance:
        good_jack_club.append([m])
similar.append((len(good_jack_club)))

good_10_club = []
for m, n in matches_10_club:
    if m.distance < 0.8*n.distance:
        good_10_club.append([m])
similar.append((len(good_10_club)))

good_9_club = []
for m, n in matches_9_club:
    if m.distance < 0.8*n.distance:
        good_9_club.append([m])
similar.append((len(good_9_club)))

good_8_club = []
for m, n in matches_8_club:
    if m.distance < 0.8*n.distance:
        good_8_club.append([m])
similar.append((len(good_8_club)))

good_7_club = []
for m, n in matches_7_club:
    if m.distance < 0.8*n.distance:
        good_7_club.append([m])
similar.append((len(good_7_club)))

good_6_club = []
for m, n in matches_6_club:
    if m.distance < 0.8*n.distance:
        good_6_club.append([m])
similar.append((len(good_6_club)))

print(*similar)
#--------------------------------------------------------------------------------------

'''img4 = cv2.drawMatchesKnn(img_1, kp_1, img_queen_heart, kp_queen_heart, good_queen_heart, None, flags=2)
cv2.imshow('a', img7)'''

maximum = max(similar)

if maximum == similar[0]:
    num = 9
    suit = 'heart'
    print('ace_heart')
elif maximum == similar[1]:
    num = 8
    suit = 'heart'
    print('king_heart')
elif maximum == similar[2]:
    num = 7
    suit = 'heart'
    print('queen_heart')
elif maximum == similar[3]:
    num = 6
    suit = 'heart'
    print('jack_heart')
elif maximum == similar[4]:
    num = 5
    suit = 'heart'
    print('10_heart')
elif maximum == similar[5]:
    num = 4
    suit = 'heart'
    print('9_heart')
elif maximum == similar[6]:
    num = 3
    suit = 'heart'
    print('8_heart')
elif maximum == similar[7]:
    num = 2
    suit = 'heart'
    print('7_heart')
elif maximum == similar[8]:
    num = 1
    suit = 'heart'
    print('6_heart')
elif maximum == similar[9]:
    num = 9
    suit = 'spade'
    print('ace_spade')
elif maximum == similar[10]:
    num = 8
    suit = 'spade'
    print('king_spade')
elif maximum == similar[11]:
    num = 7
    suit = 'spade'
    print('queen_spade')
elif maximum == similar[12]:
    num = 6
    suit = 'spade'
    print('jack_spade')
elif maximum == similar[13]:
    num = 5
    suit = 'spade'
    print('10_spade')
elif maximum == similar[14]:
    num = 4
    suit = 'spade'
    print('9_spade')
elif maximum == similar[15]:
    num = 3
    suit = 'spade'
    print('8_spade')
elif maximum == similar[16]:
    num = 2
    suit = 'spade'
    print('7_spade')
elif maximum == similar[17]:
    num = 1
    suit = 'spade'
    print('6_spade')
elif maximum == similar[18]:
    num = 9
    suit = 'diamond'
    print('ace_diamond')
elif maximum == similar[19]:
    num = 8
    suit = 'diamond'
    print('king_diamond')
elif maximum == similar[20]:
    num = 7
    suit = 'diamond'
    print('queen_diamond')
elif maximum == similar[21]:
    num = 6
    suit = 'diamond'
    print('jack_diamond')
elif maximum == similar[22]:
    num = 5
    suit = 'diamond'
    print('10_diamond')
elif maximum == similar[23]:
    num = 4
    suit = 'diamond'
    print('9_diamond')
elif maximum == similar[24]:
    num = 3
    suit = 'diamond'
    print('8_diamond')
elif maximum == similar[25]:
    num = 2
    suit = 'diamond'
    print('7_diamond')
elif maximum == similar[26]:
    num = 1
    suit = 'diamond'
    print('6_diamond')
elif maximum == similar[28]:
    num = 9
    suit = 'club'
    print('ace_club')
elif maximum == similar[29]:
    num = 8
    suit = 'club'
    print('king_club')
elif maximum == similar[30]:
    num = 7
    suit = 'club'
    print('queen_club')
elif maximum == similar[31]:
    num = 6
    suit = 'club'
    print('jack_club')
elif maximum == similar[32]:
    num = 5
    suit = 'club'
    print('10_club')
elif maximum == similar[33]:
    num = 4
    suit = 'club'
    print('9_club')
elif maximum == similar[34]:
    num = 3
    suit = 'club'
    print('8_club')
elif maximum == similar[35]:
    num = 2
    suit = 'club'
    print('7_club')
elif maximum == similar[36]:
    num = 1
    suit = 'club'
    print('6_club')

print(num, suit)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

kp_2, des_2 = orb.detectAndCompute(img_2, None)

bf = cv2.BFMatcher()
matches_ace_heart2 = bf.knnMatch(des_2, des_ace_heart, k=2)
matches_king_heart2 = bf.knnMatch(des_2, des_king_heart, k=2)
matches_queen_heart2 = bf.knnMatch(des_2, des_queen_heart, k=2)
matches_jack_heart2 = bf.knnMatch(des_2, des_jack_heart, k=2)
matches_10_heart2 = bf.knnMatch(des_2, des_10_heart, k=2)
matches_9_heart2 = bf.knnMatch(des_2, des_9_heart, k=2)
matches_8_heart2 = bf.knnMatch(des_2, des_8_heart, k=2)
matches_7_heart2 = bf.knnMatch(des_2, des_7_heart, k=2)
matches_6_heart2 = bf.knnMatch(des_2, des_6_heart, k=2)


matches_ace_spade2 = bf.knnMatch(des_2, des_ace_spade, k=2)
matches_king_spade2 = bf.knnMatch(des_2, des_king_spade, k=2)
matches_queen_spade2 = bf.knnMatch(des_2, des_queen_spade, k=2)
matches_jack_spade2 = bf.knnMatch(des_2, des_jack_spade, k=2)
matches_10_spade2 = bf.knnMatch(des_2, des_10_spade, k=2)
matches_9_spade2 = bf.knnMatch(des_2, des_9_spade, k=2)
matches_8_spade2 = bf.knnMatch(des_2, des_8_spade, k=2)
matches_7_spade2 = bf.knnMatch(des_2, des_7_spade, k=2)
matches_6_spade2 = bf.knnMatch(des_2, des_6_spade, k=2)


matches_ace_diamond2 = bf.knnMatch(des_2, des_ace_diamond, k=2)
matches_king_diamond2 = bf.knnMatch(des_2, des_king_diamond, k=2)
matches_queen_diamond2 = bf.knnMatch(des_2, des_queen_diamond, k=2)
matches_jack_diamond2 = bf.knnMatch(des_2, des_jack_diamond, k=2)
matches_10_diamond2 = bf.knnMatch(des_2, des_10_diamond, k=2)
matches_9_diamond2 = bf.knnMatch(des_2, des_9_diamond, k=2)
matches_8_diamond2 = bf.knnMatch(des_2, des_8_diamond, k=2)
matches_7_diamond2 = bf.knnMatch(des_2, des_7_diamond, k=2)
matches_6_diamond2 = bf.knnMatch(des_2, des_6_diamond, k=2)


matches_ace_club2 = bf.knnMatch(des_2, des_ace_club, k=2)
matches_king_club2 = bf.knnMatch(des_2, des_king_club, k=2)
matches_queen_club2 = bf.knnMatch(des_2, des_queen_club, k=2)
matches_jack_club2 = bf.knnMatch(des_2, des_jack_club, k=2)
matches_10_club2 = bf.knnMatch(des_2, des_10_club, k=2)
matches_9_club2 = bf.knnMatch(des_2, des_9_club, k=2)
matches_8_club2 = bf.knnMatch(des_2, des_8_club, k=2)
matches_7_club2 = bf.knnMatch(des_2, des_7_club, k=2)
matches_6_club2 = bf.knnMatch(des_2, des_6_club, k=2)

#------------------------------------------------------------

good_ace_heart2 = []
for m, n in matches_ace_heart2:
    if m.distance < 0.8*n.distance:
        good_ace_heart2.append([m])
similar2.append((len(good_ace_heart2)))

good_king_heart2 = []
for m, n in matches_king_heart2:
    if m.distance < 0.8*n.distance:
        good_king_heart2.append([m])
similar2.append((len(good_king_heart2)))

good_queen_heart2 = []
for m, n in matches_queen_heart2:
    if m.distance < 0.8*n.distance:
        good_queen_heart2.append([m])
similar2.append((len(good_queen_heart2)))

good_jack_heart2 = []
for m, n in matches_jack_heart2:
    if m.distance < 0.8*n.distance:
        good_jack_heart2.append([m])
similar2.append((len(good_jack_heart2)))

good_10_heart2 = []
for m, n in matches_10_heart2:
    if m.distance < 0.8*n.distance:
        good_10_heart2.append([m])
similar2.append((len(good_10_heart2)))

good_9_heart2 = []
for m, n in matches_9_heart2:
    if m.distance < 0.8*n.distance:
        good_9_heart2.append([m])
similar2.append((len(good_9_heart2)))

good_8_heart2 = []
for m, n in matches_8_heart2:
    if m.distance < 0.8*n.distance:
        good_8_heart2.append([m])
similar2.append((len(good_8_heart2)))

good_7_heart2 = []
for m, n in matches_7_heart2:
    if m.distance < 0.8*n.distance:
        good_7_heart2.append([m])
similar2.append((len(good_7_heart2)))

good_6_heart2 = []
for m, n in matches_6_heart2:
    if m.distance < 0.8*n.distance:
        good_6_heart2.append([m])
similar2.append((len(good_6_heart2)))
#=====================================

good_ace_spade2 = []
for m, n in matches_ace_spade2:
    if m.distance < 0.8*n.distance:
        good_ace_spade2.append([m])
similar2.append((len(good_ace_spade2)))

good_king_spade2 = []
for m, n in matches_king_spade2:
    if m.distance < 0.8*n.distance:
        good_king_spade2.append([m])
similar2.append((len(good_king_spade2)))

good_queen_spade2 = []
for m, n in matches_queen_spade2:
    if m.distance < 0.8*n.distance:
        good_queen_spade2.append([m])
similar2.append((len(good_queen_spade2)))

good_jack_spade2 = []
for m, n in matches_jack_spade2:
    if m.distance < 0.8*n.distance:
        good_jack_spade2.append([m])
similar2.append((len(good_jack_spade2)))

good_10_spade2 = []
for m, n in matches_10_spade2:
    if m.distance < 0.8*n.distance:
        good_10_spade2.append([m])
similar2.append((len(good_10_spade2)))

good_9_spade2 = []
for m, n in matches_9_spade2:
    if m.distance < 0.8*n.distance:
        good_9_spade2.append([m])
similar2.append((len(good_9_spade2)))

good_8_spade2 = []
for m, n in matches_8_spade2:
    if m.distance < 0.8*n.distance:
        good_8_spade2.append([m])
similar2.append((len(good_8_spade2)))

good_7_spade2 = []
for m, n in matches_7_spade2:
    if m.distance < 0.8*n.distance:
        good_7_spade2.append([m])
similar2.append((len(good_7_spade2)))

good_6_spade2 = []
for m, n in matches_6_spade2:
    if m.distance < 0.8*n.distance:
        good_6_spade2.append([m])
similar2.append((len(good_6_spade2)))
#==================================

good_ace_diamond2 = []
for m, n in matches_ace_diamond2:
    if m.distance < 0.8*n.distance:
        good_ace_diamond2.append([m])
similar2.append((len(good_ace_diamond2)))

good_king_diamond2 = []
for m, n in matches_king_diamond2:
    if m.distance < 0.8*n.distance:
        good_king_diamond2.append([m])
similar2.append((len(good_king_diamond2)))

good_queen_diamond2 = []
for m, n in matches_queen_diamond2:
    if m.distance < 0.8*n.distance:
        good_queen_diamond2.append([m])
similar2.append((len(good_queen_diamond2)))

good_jack_diamond2 = []
for m, n in matches_jack_diamond2:
    if m.distance < 0.8*n.distance:
        good_jack_diamond2.append([m])
similar2.append((len(good_jack_diamond2)))

good_10_diamond2 = []
for m, n in matches_10_diamond2:
    if m.distance < 0.8*n.distance:
        good_10_diamond2.append([m])
similar2.append((len(good_10_diamond2)))

good_9_diamond2 = []
for m, n in matches_9_diamond2:
    if m.distance < 0.8*n.distance:
        good_9_diamond2.append([m])
similar2.append((len(good_9_diamond2)))

good_8_diamond2 = []
for m, n in matches_8_diamond2:
    if m.distance < 0.8*n.distance:
        good_8_diamond2.append([m])
similar2.append((len(good_8_diamond2)))

good_7_diamond2 = []
for m, n in matches_7_diamond2:
    if m.distance < 0.8*n.distance:
        good_7_diamond2.append([m])
similar2.append((len(good_7_diamond2)))

good_6_diamond2 = []
for m, n in matches_6_diamond2:
    if m.distance < 0.8*n.distance:
        good_6_diamond2.append([m])
similar2.append((len(good_6_diamond2)))
#===================================

good_ace_club2 = []
for m, n in matches_ace_club2:
    if m.distance < 0.8*n.distance:
        good_ace_club2.append([m])
similar2.append((len(good_ace_club2)))

good_king_club2 = []
for m, n in matches_king_club2:
    if m.distance < 0.8*n.distance:
        good_king_club2.append([m])
similar2.append((len(good_king_club2)))

good_queen_club2 = []
for m, n in matches_queen_club2:
    if m.distance < 0.8*n.distance:
        good_queen_club2.append([m])
similar2.append((len(good_queen_club2)))

good_jack_club2 = []
for m, n in matches_jack_club2:
    if m.distance < 0.8*n.distance:
        good_jack_club2.append([m])
similar2.append((len(good_jack_club2)))

good_10_club2 = []
for m, n in matches_10_club2:
    if m.distance < 0.8*n.distance:
        good_10_club2.append([m])
similar2.append((len(good_10_club2)))

good_9_club2 = []
for m, n in matches_9_club2:
    if m.distance < 0.8*n.distance:
        good_9_club2.append([m])
similar2.append((len(good_9_club2)))

good_8_club2 = []
for m, n in matches_8_club2:
    if m.distance < 0.8*n.distance:
        good_8_club2.append([m])
similar2.append((len(good_8_club2)))

good_7_club2 = []
for m, n in matches_7_club2:
    if m.distance < 0.8*n.distance:
        good_7_club2.append([m])
similar2.append((len(good_7_club2)))

good_6_club2 = []
for m, n in matches_6_club2:
    if m.distance < 0.8*n.distance:
        good_6_club2.append([m])
similar2.append((len(good_6_club2)))

print(*similar2)
maximum2 = max(similar2)

if maximum2 == similar2[0]:
    num2 = 9
    suit2 = 'heart'
    print('ace_heart')
elif maximum2 == similar2[1]:
    num2 = 8
    suit2 = 'heart'
    print('king_heart')
elif maximum2 == similar2[2]:
    num2 = 7
    suit2 = 'heart'
    print('queen_heart')
elif maximum2 == similar2[3]:
    num2 = 6
    suit2 = 'heart'
    print('jack_heart')
elif maximum2 == similar2[4]:
    num2 = 5
    suit2 = 'heart'
    print('10_heart')
elif maximum2 == similar2[5]:
    num2 = 4
    suit2 = 'heart'
    print('9_heart')
elif maximum2 == similar2[6]:
    num2 = 3
    suit2 = 'heart'
    print('8_heart')
elif maximum2 == similar2[7]:
    num2 = 2
    suit2 = 'heart'
    print('7_heart')
elif maximum2 == similar2[8]:
    num2 = 1
    suit2 = 'heart'
    print('6_heart')
elif maximum2 == similar2[9]:
    num2 = 9
    suit2 = 'spade'
    print('ace_spade')
elif maximum2 == similar2[10]:
    num2 = 8
    suit2 = 'spade'
    print('king_spade')
elif maximum2 == similar2[11]:
    num2 = 7
    suit2 = 'spade'
    print('queen_spade')
elif maximum2 == similar2[12]:
    num2 = 6
    suit2 = 'spade'
    print('jack_spade')
elif maximum2 == similar2[13]:
    num2 = 5
    suit2 = 'spade'
    print('10_spade')
elif maximum2 == similar2[14]:
    num2 = 4
    suit2 = 'spade'
    print('9_spade')
elif maximum2 == similar2[15]:
    num2 = 3
    suit2 = 'spade'
    print('8_spade')
elif maximum2 == similar2[16]:
    num2 = 2
    suit2 = 'spade'
    print('7_spade')
elif maximum2 == similar2[17]:
    num2 = 1
    suit2 = 'spade'
    print('6_spade')
elif maximum2 == similar2[18]:
    num2 = 9
    suit2 = 'diamond'
    print('ace_diamond')
elif maximum2 == similar2[19]:
    num2 = 8
    suit2 = 'diamond'
    print('king_diamond')
elif maximum2 == similar2[20]:
    num2 = 7
    suit2 = 'diamond'
    print('queen_diamond')
elif maximum2 == similar2[21]:
    num2 = 6
    suit2 = 'diamond'
    print('jack_diamond')
elif maximum2 == similar2[22]:
    num2 = 5
    suit2 = 'diamond'
    print('10_diamond')
elif maximum2 == similar2[23]:
    num2 = 4
    suit2 = 'diamond'
    print('9_diamond')
elif maximum2 == similar2[24]:
    num2 = 3
    suit2 = 'diamond'
    print('8_diamond')
elif maximum2 == similar2[25]:
    num2 = 2
    suit2 = 'diamond'
    print('7_diamond')
elif maximum2 == similar2[26]:
    num2 = 1
    suit2 = 'diamond'
    print('6_diamond')
elif maximum2 == similar2[28]:
    num2 = 9
    suit2 = 'club'
    print('ace_club')
elif maximum2 == similar2[29]:
    num2 = 8
    suit2 = 'club'
    print('king_club')
elif maximum2 == similar2[30]:
    num2 = 7
    suit2 = 'club'
    print('queen_club')
elif maximum2 == similar2[31]:
    num2 = 6
    suit2 = 'club'
    print('jack_club')
elif maximum2 == similar2[32]:
    num2 = 5
    suit2 = 'club'
    print('10_club')
elif maximum2 == similar2[33]:
    num2 = 4
    suit2 = 'club'
    print('9_club')
elif maximum2 == similar2[34]:
    num2 = 3
    suit2 = 'club'
    print('8_club')
elif maximum2 == similar2[35]:
    num2 = 2
    suit2 = 'club'
    print('7_club')
elif maximum2 == similar2[36]:
    num2 = 1
    suit2 = 'club'
    print('6_club')

print(num2, suit2)
cv2.waitKey(0)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


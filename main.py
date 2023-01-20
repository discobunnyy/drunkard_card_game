import cv2

similar = []

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
img5 = cv2.drawMatchesKnn(img_1, kp_1, img_ace_heart, kp_ace_heart, good_ace_heart, None, flags=2)
img7 = cv2.drawMatchesKnn(img_1, kp_1, img_ace_spade, kp_ace_spade, good_ace_spade, None, flags=2)

cv2.imshow('c', img4)
cv2.imshow('d', img5)
cv2.imshow('a', img7)'''

maximum = max(similar)

if maximum == similar[0]:
    print('ace_heart')
elif maximum == similar[1]:
    print('king_heart')
elif maximum == similar[2]:
    print('queen_heart')
elif maximum == similar[3]:
    print('jack_heart')
elif maximum == similar[4]:
    print('10_heart')
elif maximum == similar[5]:
    print('9_heart')
elif maximum == similar[6]:
    print('8_heart')
elif maximum == similar[7]:
    print('7_heart')
elif maximum == similar[8]:
    print('6_heart')
elif maximum == similar[9]:
    print('ace_spade')
elif maximum == similar[10]:
    print('king_spade')
elif maximum == similar[11]:
    print('queen_spade')
elif maximum == similar[12]:
    print('jack_spade')
elif maximum == similar[13]:
    print('10_spade')
elif maximum == similar[14]:
    print('9_spade')
elif maximum == similar[15]:
    print('8_spade')
elif maximum == similar[16]:
    print('7_spade')
elif maximum == similar[17]:
    print('6_spade')
elif maximum == similar[18]:
    print('ace_diamond')
elif maximum == similar[19]:
    print('king_diamond')
elif maximum == similar[20]:
    print('queen_diamond')
elif maximum == similar[21]:
    print('jack_diamond')
elif maximum == similar[22]:
    print('10_diamond')
elif maximum == similar[23]:
    print('9_diamond')
elif maximum == similar[24]:
    print('8_diamond')
elif maximum == similar[25]:
    print('7_diamond')
elif maximum == similar[26]:
    print('6_diamond')
elif maximum == similar[28]:
    print('ace_club')
elif maximum == similar[29]:
    print('king_club')
elif maximum == similar[30]:
    print('queen_club')
elif maximum == similar[31]:
    print('jack_club')
elif maximum == similar[32]:
    print('10_club')
elif maximum == similar[33]:
    print('9_club')
elif maximum == similar[34]:
    print('8_club')
elif maximum == similar[35]:
    print('7_club')
elif maximum == similar[36]:
    print('6_club')


cv2.waitKey(0)

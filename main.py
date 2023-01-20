import cv2

sim = []

img_1 = cv2.imread('cards/example.png', 0)
img_2 = cv2.imread('cards/king_heart.png', 0)
img_queen_heart = cv2.imread('cards/queen_heart.png', 0)
img_ace_heart = cv2.imread('cards/ace_heart.png', 0)
img_king_heart = cv2.imread('cards/king_heart.png', 0)
img_ace_spade = cv2.imread('cards/ace_spade.png', 0)
img_ace_diamond = cv2.imread('cards/ace_diamond.png', 0)
img_ace_club = cv2.imread('cards/ace_club.png', 0)
img_jack_heart = cv2.imread('cards/jack_heart.png', 0)
img_10_heart = cv2.imread('cards/10_heart.png', 0)
img_9_heart = cv2.imread('cards/9_heart.png', 0)
img_8_heart = cv2.imread('cards/8_heart.png', 0)
img_7_heart = cv2.imread('cards/7_heart.png', 0)
img_6_heart = cv2.imread('cards/6_heart.png', 0)

#------------------------------------------------
orb = cv2.ORB_create()
#------------------------------------------------

kp_1, des_1 = orb.detectAndCompute(img_1, None)
kp_queen_heart, des_queen_heart = orb.detectAndCompute(img_queen_heart, None)
kp_ace_heart, des_ace_heart = orb.detectAndCompute(img_ace_heart, None)
kp_king_heart, des_king_heart = orb.detectAndCompute(img_king_heart, None)
kp_ace_spade, des_ace_spade = orb.detectAndCompute(img_ace_spade, None)
kp_ace_diamond, des_ace_diamond = orb.detectAndCompute(img_ace_diamond, None)
kp_ace_club, des_ace_club = orb.detectAndCompute(img_ace_club, None)
kp_jack_heart, des_jack_heart = orb.detectAndCompute(img_jack_heart, None)
kp_10_heart, des_10_heart = orb.detectAndCompute(img_10_heart, None)
kp_9_heart, des_9_heart = orb.detectAndCompute(img_9_heart, None)
kp_8_heart, des_8_heart = orb.detectAndCompute(img_8_heart, None)
kp_7_heart, des_7_heart = orb.detectAndCompute(img_7_heart, None)
kp_6_heart, des_6_heart = orb.detectAndCompute(img_6_heart, None)

#------------------------------------------------
bf = cv2.BFMatcher()
matches_queen_heart = bf.knnMatch(des_1, des_queen_heart, k=2)
matches_ace_heart = bf.knnMatch(des_1, des_ace_heart, k=2)
matches_king_heart = bf.knnMatch(des_1, des_king_heart, k=2)
matches_ace_spade = bf.knnMatch(des_1, des_ace_spade, k=2)
matches_ace_diamond = bf.knnMatch(des_1, des_ace_diamond, k=2)
matches_ace_club = bf.knnMatch(des_1, des_ace_club, k=2)
matches_jack_heart = bf.knnMatch(des_1, des_jack_heart, k=2)
matches_10_heart = bf.knnMatch(des_1, des_10_heart, k=2)
matches_9_heart = bf.knnMatch(des_1, des_9_heart, k=2)
matches_8_heart = bf.knnMatch(des_1, des_8_heart, k=2)
matches_7_heart = bf.knnMatch(des_1, des_7_heart, k=2)
matches_6_heart = bf.knnMatch(des_1, des_6_heart, k=2)

#------------------------------------------------------

good_queen_heart = []
for m, n in matches_queen_heart:
    if m.distance < 0.8*n.distance:
        good_queen_heart.append([m])
sim.append((len(good_queen_heart)))
print(*sim)


good_ace_heart = []
for m, n in matches_ace_heart:
    if m.distance < 0.8*n.distance:
        good_ace_heart.append([m])
sim.append((len(good_ace_heart)))
print(*sim)


good_king_heart = []
for m, n in matches_king_heart:
    if m.distance < 0.8*n.distance:
        good_king_heart.append([m])
sim.append((len(good_king_heart)))
print(*sim)


good_ace_spade = []
for m, n in matches_ace_spade:
    if m.distance < 0.8*n.distance:
        good_ace_spade.append([m])
sim.append((len(good_ace_spade)))
print(*sim)


good_ace_diamond = []
for m, n in matches_ace_diamond:
    if m.distance < 0.8*n.distance:
        good_ace_diamond.append([m])
sim.append((len(good_ace_diamond)))
print(*sim)


good_ace_club = []
for m, n in matches_ace_club:
    if m.distance < 0.8*n.distance:
        good_ace_club.append([m])
sim.append((len(good_ace_club)))
print(*sim)

good_jack_heart = []
for m, n in matches_jack_heart:
    if m.distance < 0.8*n.distance:
        good_jack_heart.append([m])
sim.append((len(good_jack_heart)))
print(*sim)

good_10_heart = []
for m, n in matches_10_heart:
    if m.distance < 0.8*n.distance:
        good_10_heart.append([m])
sim.append((len(good_10_heart)))
print(*sim)

good_9_heart = []
for m, n in matches_9_heart:
    if m.distance < 0.8*n.distance:
        good_9_heart.append([m])
sim.append((len(good_9_heart)))
print(*sim)

good_8_heart = []
for m, n in matches_8_heart:
    if m.distance < 0.8*n.distance:
        good_8_heart.append([m])
sim.append((len(good_8_heart)))
print(*sim)

good_7_heart = []
for m, n in matches_7_heart:
    if m.distance < 0.8*n.distance:
        good_7_heart.append([m])
sim.append((len(good_7_heart)))
print(*sim)

good_6_heart = []
for m, n in matches_6_heart:
    if m.distance < 0.8*n.distance:
        good_6_heart.append([m])
sim.append((len(good_6_heart)))
print(*sim)




img4 = cv2.drawMatchesKnn(img_1, kp_1, img_queen_heart, kp_queen_heart, good_queen_heart, None, flags=2)
img5 = cv2.drawMatchesKnn(img_1, kp_1, img_ace_heart, kp_ace_heart, good_ace_heart, None, flags=2)
img7 = cv2.drawMatchesKnn(img_1, kp_1, img_ace_spade, kp_ace_spade, good_ace_spade, None, flags=2)

cv2.imshow('c', img4)
cv2.imshow('d', img5)
cv2.imshow('a', img7)
cv2.waitKey(0)

from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase
from random import randint, randrange
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


from math import ceil, floor, factorial, log10
# from math import log,sqrt,cos,tan,sin,radians
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
# from decimal import *
# from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
# from collections import OrderedDict
# from itertools import permutations


M=1000000007
# M=998244353
# INF = float("inf")
INF = 9223372036854775807
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================
N = 1001
memo = [[[-1]*2 for _ in range(N)] for _ in range(N)]
def f(a, b, player):
    if memo[a][b][player] != -1: return memo[a][b][player]
    if a == 0 and b == 0: return player^1
    for x in range(1, a+1):
        p = f(a-x, b, player^1)
        if p == player:
            memo[a][b][player] = player
            return player
    for x in range(1, b+1):
        p = f(a, b-x, player^1)
        if p == player:
            memo[a][b][player] = player
            return player
    for x in range(1, 1+min(a, b)):
        p = f(a-x, b-x, player^1)
        if p == player:
            memo[a][b][player] = player
            return player
    memo[a][b][player] = player^1
    return player^1

# for p in range(2):
#     for i in range(21):
#         for j in range(21):
#             # f(i, j, p)
#             print(f(i, j, p), end=' ')
#         print()
#     print()


one = '''1 2
2 1
3 5
4 7
5 3
6 10
7 4
8 13
9 15
10 6
11 18
12 20
13 8
14 23
15 9
16 26
17 28
18 11
19 31
20 12
21 34
22 36
23 14
24 39
25 41
26 16
27 44
28 17
29 47
30 49
31 19
32 52
33 54
34 21
35 57
36 22
37 60
38 62
39 24
40 65
41 25
42 68
43 70
44 27
45 73
46 75
47 29
48 78
49 30
50 81
51 83
52 32
53 86
54 33
55 89
56 91
57 35
58 94
59 96
60 37
61 99
62 38
63 102
64 104
65 40
66 107
67 109
68 42
69 112
70 43
71 115
72 117
73 45
74 120
75 46
76 123
77 125
78 48
79 128
80 130
81 50
82 133
83 51
84 136
85 138
86 53
87 141
88 143
89 55
90 146
91 56
92 149
93 151
94 58
95 154
96 59
97 157
98 159
99 61
100 162
101 164
102 63
103 167
104 64
105 170
106 172
107 66
108 175
109 67
110 178
111 180
112 69
113 183
114 185
115 71
116 188
117 72
118 191
119 193
120 74
121 196
122 198
123 76
124 201
125 77
126 204
127 206
128 79
129 209
130 80
131 212
132 214
133 82
134 217
135 219
136 84
137 222
138 85
139 225
140 227
141 87
142 230
143 88
144 233
145 235
146 90
147 238
148 240
149 92
150 243
151 93
152 246
153 248
154 95
155 251
156 253
157 97
158 256
159 98
160 259
161 261
162 100
163 264
164 101
165 267
166 269
167 103
168 272
169 274
170 105
171 277
172 106
173 280
174 282
175 108
176 285
177 287
178 110
179 290
180 111
181 293
182 295
183 113
184 298
185 114
186 301
187 303
188 116
189 306
190 308
191 118
192 311
193 119
194 314
195 316
196 121
197 319
198 122
199 322
200 324
201 124
202 327
203 329
204 126
205 332
206 127
207 335
208 337
209 129
210 340
211 342
212 131
213 345
214 132
215 348
216 350
217 134
218 353
219 135
220 356
221 358
222 137
223 361
224 363
225 139
226 366
227 140
228 369
229 371
230 142
231 374
232 376
233 144
234 379
235 145
236 382
237 384
238 147
239 387
240 148
241 390
242 392
243 150
244 395
245 397
246 152
247 400
248 153
249 403
250 405
251 155
252 408
253 156
254 411
255 413
256 158
257 416
258 418
259 160
260 421
261 161
262 424
263 426
264 163
265 429
266 431
267 165
268 434
269 166
270 437
271 439
272 168
273 442
274 169
275 445
276 447
277 171
278 450
279 452
280 173
281 455
282 174
283 458
284 460
285 176
286 463
287 177
288 466
289 468
290 179
291 471
292 473
293 181
294 476
295 182
296 479
297 481
298 184
299 484
300 486
301 186
302 489
303 187
304 492
305 494
306 189
307 497
308 190
309 500
310 502
311 192
312 505
313 507
314 194
315 510
316 195
317 513
318 515
319 197
320 518
321 520
322 199
323 523
324 200
325 526
326 528
327 202
328 531
329 203
330 534
331 536
332 205
333 539
334 541
335 207
336 544
337 208
338 547
339 549
340 210
341 552
342 211
343 555
344 557
345 213
346 560
347 562
348 215
349 565
350 216
351 568
352 570
353 218
354 573
355 575
356 220
357 578
358 221
359 581
360 583
361 223
362 586
363 224
364 589
365 591
366 226
367 594
368 596
369 228
370 599
371 229
372 602
373 604
374 231
375 607
376 232
377 610
378 612
379 234
380 615
381 617
382 236
383 620
384 237
385 623
386 625
387 239
388 628
389 630
390 241
391 633
392 242
393 636
394 638
395 244
396 641
397 245
398 644
399 646
400 247
401 649
402 651
403 249
404 654
405 250
406 657
407 659
408 252
409 662
410 664
411 254
412 667
413 255
414 670
415 672
416 257
417 675
418 258
419 678
420 680
421 260
422 683
423 685
424 262
425 688
426 263
427 691
428 693
429 265
430 696
431 266
432 699
433 701
434 268
435 704
436 706
437 270
438 709
439 271
440 712
441 714
442 273
443 717
444 719
445 275
446 722
447 276
448 725
449 727
450 278
451 730
452 279
453 733
454 735
455 281
456 738
457 740
458 283
459 743
460 284
461 746
462 748
463 286
464 751
465 753
466 288
467 756
468 289
469 759
470 761
471 291
472 764
473 292
474 767
475 769
476 294
477 772
478 774
479 296
480 777
481 297
482 780
483 782
484 299
485 785
486 300
487 788
488 790
489 302
490 793
491 795
492 304
493 798
494 305
495 801
496 803
497 307
498 806
499 808
500 309
501 811
502 310
503 814
504 816
505 312
506 819
507 313
508 822
509 824
510 315
511 827
512 829
513 317
514 832
515 318
516 835
517 837
518 320
519 840
520 321
521 843
522 845
523 323
524 848
525 850
526 325
527 853
528 326
529 856
530 858
531 328
532 861
533 863
534 330
535 866
536 331
537 869
538 871
539 333
540 874
541 334
542 877
543 879
544 336
545 882
546 884
547 338
548 887
549 339
550 890
551 892
552 341
553 895
554 897
555 343
556 900
557 344
558 903
559 905
560 346
561 908
562 347
563 911
564 913
565 349
566 916
567 918
568 351
569 921
570 352
571 924
572 926
573 354
574 929
575 355
576 932
577 934
578 357
579 937
580 939
581 359
582 942
583 360
584 945
585 947
586 362
587 950
588 952
589 364
590 955
591 365
592 958
593 960
594 367
595 963
596 368
597 966
598 968
599 370
600 971
601 973
602 372
603 976
604 373
605 979
606 981
607 375
608 984
609 986
610 377
611 989
612 378
613 992
614 994
615 380
616 997
617 381
618 1000
620 383
623 385
625 386
628 388
630 389
633 391
636 393
638 394
641 396
644 398
646 399
649 401
651 402
654 404
657 406
659 407
662 409
664 410
667 412
670 414
672 415
675 417
678 419
680 420
683 422
685 423
688 425
691 427
693 428
696 430
699 432
701 433
704 435
706 436
709 438
712 440
714 441
717 443
719 444
722 446
725 448
727 449
730 451
733 453
735 454
738 456
740 457
743 459
746 461
748 462
751 464
753 465
756 467
759 469
761 470
764 472
767 474
769 475
772 477
774 478
777 480
780 482
782 483
785 485
788 487
790 488
793 490
795 491
798 493
801 495
803 496
806 498
808 499
811 501
814 503
816 504
819 506
822 508
824 509
827 511
829 512
832 514
835 516
837 517
840 519
843 521
845 522
848 524
850 525
853 527
856 529
858 530
861 532
863 533
866 535
869 537
871 538
874 540
877 542
879 543
882 545
884 546
887 548
890 550
892 551
895 553
897 554
900 556
903 558
905 559
908 561
911 563
913 564
916 566
918 567
921 569
924 571
926 572
929 574
932 576
934 577
937 579
939 580
942 582
945 584
947 585
950 587
952 588
955 590
958 592
960 593
963 595
966 597
968 598
971 600
973 601
976 603
979 605
981 606
984 608
986 609
989 611
992 613
994 614
997 616
1000 618'''


def main():
    TestCases = 1
    TestCases = int(input())
    dp0 = [[0] * N for _ in range(N)]
    dp1 = [[0] * N for _ in range(N)]
    dp0[0][0] = 1
    dp1[0][0] = 0

    for line in one.split('\n'):
        a, b = [int(i) for i in line.split()]
        dp0[a][b] = 1
        dp1[a][b] = 0

    
    for _ in range(TestCases):
        a, b = [int(i) for i in input().split()]
        # win = f(a, b, 0)
        win = dp0[a][b]
        print('Abhishek Bachchan' if win else 'Salman Khan')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# ======================== Functions declaration Starts ========================
abc='abcdefghijklmnopqrstuvwxyz'
abd={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def copy2d(lst): return [x[:] for x in lst]   #Copy 2D list... Avoid Using Deepcopy
def no_of_digits(num): return 0 if num <= 0 else int(log10(num)) + 1
def powm(num, power, mod=M): return pow(num, power, mod)
def isPowerOfTwo(x): return (x and (not(x & (x - 1))))
def LSB(num):
    """Returns Least Significant Bit of a number (Rightmost bit) in O(1)"""
    return num & -num

def MSB(num):
    """Returns Most Significant Bit of a number (Leftmost bit) in O(logN)"""
    if num <= 0: return 0
    ans = 1; num >>= 1
    while num:
        num >>= 1; ans <<= 1
    return ans


LB = bisect_left   # Lower bound
UB = bisect_right  # Upper bound
 
def BS(a, x):      # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x*y)//gcd(x,y)


# import threading
# def dmain():
#     sys.setrecursionlimit(1000000)
#     threading.stack_size(1024000)
#     thread = threading.Thread(target=main)
#     thread.start()
            
# =============================== Custom Classes ===============================

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ R
Int = lambda x:Wrapper(int(x))        

class myDict():
    def __init__(self,func=int):
        # self.RANDOM = randint(0,1<<32)
        self.RANDOM = R
        self.default=func
        self.dict={}
    def __getitem__(self,key):
        myKey=self.RANDOM^key
        if myKey not in self.dict:
            self.dict[myKey]=self.default()
        return self.dict[myKey]
    def __setitem__(self,key,item):
        myKey=self.RANDOM^key
        self.dict[myKey]=item
    def __contains__(self,key):
        myKey=self.RANDOM^key
        return myKey in self.dict
    def __delitem__(self,key):
        myKey=self.RANDOM^key
        del self.dict[myKey]
    def keys(self):
        return [self.RANDOM^i for i in self.dict]


# =============================== Region Fastio ===============================
if not os.path.isdir('C:/users/acer'):
    BUFSIZE = 8192
    
    
    class FastIO(IOBase):
        newlines = 0
    
        def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None
    
        def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()
    
        def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()
    
        def flush(self):
            if self.writable:
                os.write(self._fd, self.buffer.getvalue())
                self.buffer.truncate(0), self.buffer.seek(0)
    
    
    class IOWrapper(IOBase):
        def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    
    
    def print(*args, **kwargs):
        """Prints the values to a stream, or to sys.stdout by default."""
        sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
        at_start = True
        for x in args:
            if not at_start:
                file.write(sep)
            file.write(str(x))
            at_start = False
        file.write(kwargs.pop("end", "\n"))
        if kwargs.pop("flush", False):
            file.flush()
    
    
    if sys.version_info[0] < 3:
        sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
    else:
        sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    
    input = lambda: sys.stdin.readline().rstrip("\r\n")

# =============================== Endregion ===============================

if __name__ == "__main__":
    #read()
    main()
    #dmain()

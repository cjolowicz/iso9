#!/usr/bin/python

'''ISO 9:1995 transliteration for Cyrillic text.

Simple usage:

    import iso9
    romanised_unicode = iso9.transliterate(cyrillic_unicode)


Copyright (c) 2008 by Mublin <mublin@dealloc.org>
This module is free software, and you may redistribute it and/or modify
it under the same terms as Python itself, so long as this copyright message
and disclaimer are retained in their original form.

IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF
THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS,
AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.'''

__author__ = "Mublin <mublin@dealloc.org>"
__date__ = "19 April 2008"
__version__ = "0.1.1"

iso9 = u'''\
\u0410	\u0430	A	a			
\u04d2	\u04d3	\xc4	\xe4	00C4	00E4	a diaeresis
\u04d2\u0304	\u04d3\u0304	\u1ea0\u0308	\u1ea1\u0308	00C4+0323	00E4+0323	a diaeresis and dot below
\u04d0	\u04d1	\u0102	\u0103	0102	0103	a breve
\u0410\u0304	\u0430\u0304	\u0100	\u0101	0100	0101	a macron
\u04d4	\u04d5	\xc6	\xe6	00C6	00E6	ae ligature
\u0410\u0301	\u0430\u0301	\xc1	\xe1	00C1	00E1	a acute
\u0410\u030a	\u0430\u030a	\xc5	\xe5	00C5	00E5	a ring
\u0411	\u0431	B	b			
\u0412	\u0432	V	v			
\u0413	\u0433	G	g			
\u0403	\u0453	\u01f4	\u01f5	01F4	01F5	g acute
\u0492	\u0493	\u0120	\u0121	0120	0121	g dot
\u0494	\u0495	\u011e	\u011f	011E	011F	g breve
\u04ba	\u04bb	\u1e24	\u1e25	1E24	1E25	h dot
\u0414	\u0434	D	d			
\u0402	\u0452	\u0110	\u0111	0110	0111	d macron
\u0415	\u0435	E	e			
\u04d6	\u04d7	\u0114	\u0115	0114	0115	e breve
\u0401	\u0451	\xcb	\xeb	00CB	00EB	e diaeresis
\u0404	\u0454	\xca	\xea	00CA	00EA	e circumflex
\u0416	\u0436	\u017d	\u017e	017D	017E	z caron
\u0496	\u0497	\u017d\u0327	\u017e\u0327	017D+0327	017E+0327	z caron and cedilla
\u04dc	\u04dd	Z\u0304	z\u0304	Z+0304	z+0304	z macron
\u04c1	\u04c2	Z\u0306	z\u0306	Z+0306	z+0306	z breve
\u0417	\u0437	Z	z			
\u04de	\u04df	Z\u0308	z\u0308	Z+0308	z+0308	z diaeresis
\u04e0	\u04e1	\u0179	\u017a	0179	017A	z acute
\u0405	\u0455	\u1e90	\u1e91	1E90	1E91	z circumflex
\u0418	\u0438	I	i			
\u04e2	\u04e3	\u012a	\u012b	012A	012B	i macron
\u0418\u0301	\u0438\u0301	\xcd	\xed	00CD	00ED	i acute
\u04e4	\u04e5	\xce	\xee	00CE	00EE	i circumflex
\u0419	\u0439	J	j			
\u0406	\u0456	\xcc	\xec	00CC	00EC	i grave
\u0407	\u0457	\xcf	\xef	00CF	00EF	i diaeresis
\u0406\u0304	\u0456\u0304	\u01cf	\u01d0	01CF (012C)	01D0 (012D)	i caron (or breve)
\u0408	\u0458	J\u030c	\u01f0	J+030C	01F0	j caron
\u0408\u0335	\u0458\u0335	J\u0301	j\u0301	J+0301	j+0301	j acute
\u041a	\u043a	K	k			
\u04c3	\u04c4	\u1e32	\u1e33	1E32	1E33	k dot below
\u049c	\u049d	K\u0302	k\u0302	K+0302	k+0302	k circumflex
\u04a0	\u04a1	\u01e8	\u01e9	01E8	01E9	k caron
\u049e	\u049f	K\u0304	k\u0304	K+0304	k+0304	k macron
\u049a	\u049b	\u0136	\u0137	0136	0137	k cedilla
\u041a\u0328	\u043a\u0328	K\u0300	k\u0300	K+0300	k+0300	k grave
\u0480	\u0481	Q	q			
\u041b	\u043b	L	l			
\u0409	\u0459	L\u0302	l\u0302	L+0302	l+0302	l circumflex
\u0508	\u0509	\u0139	\u013a	0139	013A	l acute
\u04a6	\u04a7	\u013b	\u013c	013B	013C	l cedilla
\u041c	\u043c	M	m			
\u041d	\u043d	N	n			
\u040a	\u045a	N\u0302	n\u0302	N+0302	n+0302	n circumflex
\u04a2	\u04a3	\u0145	\u0146	0145	0146	n cedilla
\u04c9	\u04ca	\u1e46	\u1e47	1E46	1E47	n dot below
\u04a4	\u04a5	\u1e44	\u1e45	1E44	1E45	n dot
\u050a	\u050b	\u01f8	\u01f9	01F8	01F9	n grave
\u04c7	\u04c8	\u0143	\u0144	0143	0144	n acute
		\u0147	\u0148	0147	0148	n caron
\u041d\u0304	\u043d\u0304	N\u0304	n\u0304	N+0304	n+0304	n macron
\u041e	\u043e	O	o			
\u04e6	\u04e7	\xd6	\xf6	00D6	00F6	o diaeresis
\u04e8	\u04e9	\xd4	\xf4	00D4	00F4	o circumflex
\u04ea	\u04eb	\u0150	\u0151	0150	0151	o double acute
\u04ea\u0304	\u04eb\u0304	\u1ecc\u0308	\u1ecd\u0308	00D6+0323	00F6+0323	o diaeresis and dot below
\u04a8	\u04a9	\xd2	\xf2	00D2	00F2	o grave
\u041e\u0301	\u043e\u0301	\xd3	\xf3	00D3	00F3	o acute
\u041e\u0304	\u043e\u0304	\u014c	\u014d	014C	014D	o macron
		\u0152	\u0153	0152	0153	oe ligature
\u041f	\u043f	P	p			
\u04a6	\u04a7	\u1e54	\u1e55	1E54	1E55	p acute
		P\u0300	p\u0300	P+0300	p+0300	p grave
\u0420	\u0440	R	r			
\u0421	\u0441	S	s			
\u04aa	\u04ab	\u015e	\u015f	015E	015F	s cedilla
\u0421\u0300	\u0441\u0300	S\u0300	s\u0300	S+0300	s+0300	s grave
\u0422	\u0442	T	t			
\u040b	\u045b	\u0106	\u0107	0106	0107	c acute
\u050e	\u050f	T\u0300	t\u0300	T+0300	t+0300	t grave
\u0422\u030c	\u0442\u030c	\u0164	\u0165	0164	0165	t caron
\u04ac	\u04ad	\u0162	\u0163	0162	0163	t cedilla
\u040c	\u045c	\u1e30	\u1e31	1E30	1E31	k acute
\u0423	\u0443	U	u			
\u04f0	\u04f1	\xdc	\xfc	00DC	00FC	u diaeresis
\u04ee	\u04ef	\u016a	\u016b	016A	016B	u macron
\u040e	\u045e	\u016c	\u016d	016C	016D	u breve
\u04f2	\u04f3	\u0170	\u0171	0170	0171	u double acute
\u0423\u0301	\u0443\u0301	\xda	\xfa	00DA	00FA	u acute
\u04f0\u0304	\u04f1\u0304	\u1ee4\u0308	\u1ee5\u0308	00DC+0323	00FC+0323	u diaeresis and dot below
\u04ae	\u04af	\xd9	\xf9	00D9	00F9	u grave
\u04b0	\u04b1	U\u0307	u\u0307	U+0307	u+0307	u dot
\u04ee\u0308	\u04ef\u0308	\u1ee4\u0304	\u1ee5\u0304	016A+0323	016B+0323	u macron and dot below
		W	w			
\u0424	\u0444	F	f			
\u0425	\u0445	H	h			
\u04b2	\u04b3	\u1e28	\u1e29	1E28	1E29	h cedilla
\u0426	\u0446	C	c			
\u04b4	\u04b5	C\u0304	c\u0304	C+0304	c+0304	c macron
\u040f	\u045f	D\u0302	d\u0302	D+0302	d+0302	d circumflex
\u0427	\u0447	\u010c	\u010d	010C	010D	c caron
\u04b6	\u04b7	\xc7	\xe7	00C7	00E7	c cedilla
\u04cb	\u04cc	C\u0323	c\u0323	C+0323	c+0323	c dot below
\u04f4	\u04f5	C\u0308	c\u0308	C+0308	c+0308	c diaeresis
\u04b8	\u04b9	\u0108	\u0109	0108	0109	c circumflex
\u0427\u0300	\u0447\u0300	C\u0300	c\u0300	C+0300	c+0300	c grave
\u04bc	\u04bd	C\u0306	c\u0306	C+0306	c+0306	c breve
\u04be	\u04bf	\xc7\u0306	\xe7\u0306	00C7+0306	00E7+0306	c cedilla and breve
\u0428	\u0448	\u0160	\u0161	0160	0161	s caron
\u0429	\u0449	\u015c	\u015d	015C	015D	s circumflex
\u042a	\u044a	\u02ba	\u02ba	02BA	02BA	double prime
\u042b	\u044b	Y	y			
\u04f8	\u04f9	\u0178	\xff	0178	00FF	y diaeresis
\u042b\u0304	\u044b\u0304	\u0232	\u0233	0232	0233	y macron
\u042c	\u044c	\u02b9	\u02b9	02B9	02B9	prime
\u042d	\u044d	\xc8	\xe8	00C8	00E8	e grave
\u04d8	\u04d9	A\u030b	a\u030b	A+030B	a+030B	a double acute
\u04da	\u04db	\xc0	\xe0	00C0	00E0	a grave
\u042e	\u044e	\xdb	\xfb	00DB	00FB	u circumflex
\u042e\u0304	\u044e\u0304	\u016e	\u016f	016E	016F	u ring
\u042f	\u044f	\xc2	\xe2	00C2	00E2	a circumflex
\u0490	\u0491	G\u0300	g\u0300	G+0300	g+0300	g grave
\u0462	\u0463	\u011a	\u011b	011A	011B	e caron
\u046a	\u046b	\u01cd	\u01ce	01CD	01CE	a caron
\u0472	\u0473	F\u0300	f\u0300	F+0300	f+0300	f grave
\u0474	\u0475	\u1ef2	\u1ef3	1EF2	1EF3	y grave
\u04c0	\u04c0	\u2021	\u2021	2021	2021	double dagger
\u2019	\u2019	\u2019	\u2019	2019	2019	apostrophe
		\xa8	\xa8	00A8	00A8	diaeresis'''

iso9 = [line.split('\t') for line in iso9.split('\n')]

iso9, _iso9 = {}, iso9
for cyrmaj, cyrmin, latmaj, latmin, unicode1, unicode2, description in _iso9:
    iso9[cyrmaj] = latmaj
    iso9[cyrmin] = latmin

def transliterate(source):
    result = []
    for char in source:
        try:
            result.append(iso9[char])
        except KeyError:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    import sys
    for line in sys.stdin:
        sys.stdout.write(
            transliterate(line.decode('utf-8')).encode('utf-8'))

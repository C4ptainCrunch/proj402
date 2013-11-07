# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.db.models import Avg
from documents.models import Document
from django.shortcuts import get_object_or_404, render
from search.models import WordEntry
from math import log

def search_(request):
    if 'q' not in request.GET or request.GET['q'] == '':
        return render(request, 'search.tpl', {'msg': 'You searched nothing!'})
    
    request = request.GET['q'].split()
    exclude = [ q[1:] for q in filter(lambda q: q[0] == '-', request)]
    query = filter(lambda q: q[0] != '-', request)
    if len(query) == 0:
        return render(request, 'search.tpl', {'msg': 'You searched nothing!'})
    doc_list = lambda q: [we.document for we in WordEntry.objects.filter(word=q)]
    make_list = lambda list: [ doc_list(q) for q in list ]
    docs, exclude = make_list(query), make_list(exclude)
    minify = lambda l: reduce(lambda d1, d2: set(d1) & set(d2), l)
    bag = set(minify(docs))
    if len(exclude) != 0:
        bag -= set(minify(exclude))
    N = float(Document.objects.count())
    k1 = 1.6
    b = 0.75
    avg = Document.objects.aggregate(Avg('words')).values()[0]

    tf = lambda q, D: float(WordEntry.objects.get(word=q, document=D).count)
    tf_norm = lambda q, D: tf(q, D) * (k1 + 1) / (tf(q, D) + k1 * (1 - b + b * float(D.words) / avg))
    idf = lambda q: max(log(N / (WordEntry.objects.filter(word=q).count() +0.5) - 1), 0)
    idf_cache = dict((q, idf(q)) for q in query)
    for D in bag:
        D.score = sum([ idf_cache[q] * tf_norm(q, D) for q in query])
    return render(request, 'search.tpl', {'query': ' '.join(request), 'docs': sorted(bag, key=lambda x: x.score, reverse=True)})

def search(request):
#    try:
        return search_(request)
#    except Exception as e:
#        print str(e)

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from documents.models import Document
from django.shortcuts import get_object_or_404, render
from search.models import WordEntry

def search(request):
    if 'q' not in request.GET or request.GET['q'] == '':
        return render(request, 'search.tpl', {'msg': 'You searched nothing!'})
    
    query, word_list, rejected = request.GET['q'].split(), list(), list()
    for keyword in query:
        entries = WordEntry.objects.filter(word=keyword)
        if len(entries):
            docs = list()
            for entry in entries:
                docs.append((entry.document.id, entry.count, 
                             entry.document.words, 
                             entry.document.words/entry.count))
            word_list.append((keyword, docs))
        else:
            rejected.append(keyword)

    return render(request, 'search.tpl', {'rejected': rejected,
                                          'word_list': word_list})

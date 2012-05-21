# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.db import models
from django.contrib.auth.models import User

CAT_THREADS = (
    ('Q', 'Question'),
    ('C', 'Comment'),
    ('R', 'Rant'),
    ('E', 'Erratum'),
    ('G', 'Garbage'),
)

# This is duplicated in upvotes.url and course_show JS                                   
CAT_DOCUMENTS = (
    ('O', 'Official Support'),
    ('R', 'Reference'),
    ('S', 'Summary'),
    ('T', 'Exercises'),
    ('L', 'Solutions'),
    ('E', 'Old Exam'),
    ('P', 'Project'),
    ('D', 'Others'),
)

REF_DOCUMENTS = {'R': 'cat_reference', 'O': 'cat_support', 'S': 'cat_summary', 
                 'E': 'cat_exam', 'P': 'cat_project', 'L': 'cat_solution', 
                 'D': 'cat_others', 'T': 'cat_exercice'}

RESSOURCES = (
    ('D', 'Document'),
    ('T', 'Thread'),
    ('P', 'Post'),
)

class VotePost(models.Model):
    score = models.IntegerField(null=False)

class VoteThread(models.Model):
    category = models.CharField(max_length=1, choices=CAT_THREADS)
    score = models.IntegerField(null=False, default=0)

    cat_question = models.IntegerField(null=False, default=0)
    cat_comment = models.IntegerField(null=False, default=0)
    cat_rant = models.IntegerField(null=False, default=0)
    cat_erratum = models.IntegerField(null=False, default=0)
    cat_garbage = models.IntegerField(null=False, default=0)

class VoteDocument(models.Model):
    category = models.CharField(max_length=1, choices=CAT_DOCUMENTS, default="O")
    score = models.IntegerField(null=False, default=0)
    
    cat_reference = models.IntegerField(null=False, default=0)
    cat_support = models.IntegerField(null=False, default=0)
    cat_summary = models.IntegerField(null=False, default=0)
    cat_exam = models.IntegerField(null=False, default=0)
    cat_project = models.IntegerField(null=False, default=0)
    cat_solution = models.IntegerField(null=False, default=0)
    cat_exercice = models.IntegerField(null=False, default=0)
    cat_others = models.IntegerField(null=False, default=0)

    def full_category(self):
        return [ v for k, v in CAT_DOCUMENTS if k == self.category ][0]

class VoteHistory(models.Model):
    voter = models.ForeignKey(User)
    ressource = models.CharField(max_length=1, choices=RESSOURCES)
    resid = models.IntegerField(null=False)
    cat = models.CharField(max_length=1, null=True)
    score = models.IntegerField(null=False)

    class Meta:
        unique_together = ('voter', 'ressource', 'resid')

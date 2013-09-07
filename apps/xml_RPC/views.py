#!/usr/bin/python
#-*- coding=utf-8 -*-
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from models import  FileSource
from xmlrpc_method import SingleLiveSource

@login_required
def showSource(request, template_name) :
    livesource_list = SingleLiveSource.getInstance().getNames()
    filesource_list = FileSource.objects.all()
    ctx = {}
    ctx.update({
        "LiveSource": livesource_list,
        "FileSource": filesource_list,
        })
    return render_to_response(template_name, RequestContext(request, ctx))

@login_required  
def playSource(request, **kwargs):
    template_name = kwargs.pop("template_name")
    source_name = kwargs.pop("source_name")
    ctx = {}
    ctx.update({
        "template_name": template_name,
        "source_name": source_name})
    return render_to_response(template_name, RequestContext(request, ctx))



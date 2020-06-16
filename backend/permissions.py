#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 11:16:40
# Last Modified time: Tue 16 June 2020 12:04:40 

# Description:from rest_framework import permissions


class NormalUserListRetrieveOnly(permissions.BasePermission):
    """
    Global permission check for staff users.
    """
    def has_permission(self, request, view):
        if not request.user.is_staff and not request.user.is_superuser:
            if request.method == 'GET':
                return True
            else:
                return False
        else:
            return True


class NormalUserIsCurrentUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and not request.user.is_staff and not request.user.is_superuser:
            if request.method == 'GET':
                return obj.pk == request.user.id
            else:
                return False
        else:
            return True


class IsSuperStaff(permissions.BasePermission):
    """
    Global permission check for staff users.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.is_superuser
        else:
            return False

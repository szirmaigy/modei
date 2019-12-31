#!/usr/bin/python3
# -*- coding: utf-8 -*-

from domain_validation.whois import WHOIS

class DInfo():
    def __init__(self, DomainName):
        self.DomainName = str(DomainName)
        # whois = WHOIS(DomainName)
        # CreationDate = whois.creation_date()
        # Registrar = whois.registrar()
        # print(whois.creation_date())
        # return Registrar

    def DomainCreationInfo(self):
        whois = WHOIS(self.DomainName)
        CreationDate = str(whois.creation_date())
        Registrar = whois.registrar()
        return Registrar

    def IPaddress(self):
        pass

    def DNSinfo(self):
        pass


DomainName = 'google.com'
DInfo.DomainCreationInfo(DomainName)
# DInfo.DomainCreationInfo(test)

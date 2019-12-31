#!/usr/bin/python3
# -*- coding: utf-8 -*-

from domain_validation.whois import WHOIS
import dns.resolver

class DInfo():
    def __init__(self, DomainName):
        self.DomainName = DomainName

    def DomainCreationInfo(self):
        whois = WHOIS(self.DomainName)
        self.whois = whois
        CreationDate = str(self.whois.creation_date())
        Registrar = self.whois.registrar()
        return Registrar, CreationDate

    def IPaddress(self):
        ip4result = dns.resolver.query(self.DomainName, 'A')
        for ipval in ip4result:
            IP4address = ipval.to_text()
        return IP4address

    def DNSinfo(self):
        pass


DomainName = DInfo("google.com")
# DomainName.DomainCreationInfo()
DomainName.IPaddress()

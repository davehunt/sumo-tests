#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla Support
#
# The Initial Developer of the Original Code is
# Mozilla Support
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Tanay
#                 Vishal
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
import pytest

from unittestzero import Assert
import search_page


class TestSearchDecoding:

    @pytest.mark.smoketests
    @pytest.mark.bft
    @pytest.mark.fft
    @pytest.mark.prod
    def test_search_decoding(self, testsetup):
        sel                   = testsetup.selenium
        search_page_obj       = search_page.SearchPage(testsetup)

        search_term = "%3D"
        search_page_obj.go_to_search_page()
        search_page_obj.do_search_on_search_box(search_term)
        not_found = True
        counter = 0
        while not_found and counter < 3:
            if not(search_page_obj.is_search_available()):
                search_page_obj.refresh()
                counter = counter + 1
            else:
                not_found = False
        Assert.not_equal("=", sel.get_value(search_page_obj.search_box))
        Assert.equal(search_term, sel.get_value(search_page_obj.search_box))

        search_term = "%25D"
        search_page_obj.go_to_search_page()
        search_page_obj.do_search_on_search_box(search_term)
        not_found = True
        counter = 0
        while not_found and counter < 3:
            if not(search_page_obj.is_search_available()):
                search_page_obj.refresh()
                counter = counter + 1
            else:
                not_found = False
        Assert.not_equal("=", sel.get_value(search_page_obj.search_box))
        Assert.equal(search_term, sel.get_value(search_page_obj.search_box))

        search_term = "&lsquo"
        search_page_obj.go_to_search_page()
        search_page_obj.do_search_on_search_box(search_term)
        not_found = True
        counter = 0
        while not_found and counter < 3:
            if not(search_page_obj.is_search_available()):
                search_page_obj.refresh()
                counter = counter + 1
            else:
                not_found = False
        Assert.not_equal("'", sel.get_value(search_page_obj.search_box))
        Assert.equal(search_term, sel.get_value(search_page_obj.search_box))
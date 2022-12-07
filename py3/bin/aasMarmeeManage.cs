#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CmndSvc= for for setting up Marmee (Multi-Account Resident Mail Exchange Environment) AAS (Accessible Abstract Service).
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-mu"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-mu
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-mu") ; one of cs-mu, cs-u, cs-lib, b-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-mu
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/auth/bxRepos/bisos-pip/marmee/py3/bin/aasMarmeeManage.cs
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['aasMarmeeManage'], }
csInfo['version'] = '202209280025'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'aasMarmeeManage-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

csInfo['moduleDescription'] = """ #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
A =CmndSvc= for for setting up Marmee (Multi-Account Resident Mail Exchange Environment) AAS (Accessible Abstract Service).
Manages Mail Account Profiles. Sets up currents. Works with -niche.
** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:python:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= " :title "*Py Library IMPORTS*" :comment "-- with classification based framework/imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- with classification based framework/imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-mu
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

import collections
####+END:


import sys
import collections

# from bisos.marmee import marmeAcctsLib, marmeeCurrentsLib
from bisos.currents import currentsConfig

""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~csuList emacs-list Specifications~  [[elisp:(blee:org:code-block/above-run)][ /Eval Below/ ]] [[elisp:(org-cycle)][| ]]
#+BEGIN_SRC emacs-lisp
(setq  b:py:cs:csuList
  (list
   "bisos.b.cs.ro"
   "blee.csPlayer.bleep"
   ;; "bisos.marmee.marmeAcctsLib"
   "bisos.bpo.bpo"
   "bisos.bpo.bpoRunBases"
   ;; "bisos.marmee.marmeeCurrentsLib"
   "bisos.b.fpCls"
   "bisos.b.clsMethod_csu"
   "bisos.marmee.aasInMailFps"
   "bisos.marmee.aasOutMailFps"
   "bisos.marmee.aasMailFps"
   "bisos.marmee.gmailOauth2"
   "bisos.marmee.marmeeGmail"
 ))
#+END_SRC
#+RESULTS:
| bisos.b.cs.ro | blee.csPlayer.bleep | bisos.bpo.bpo | bisos.bpo.bpoRunBases | bisos.b.fpCls | bisos.b.clsMethod_csu | bisos.marmee.aasInMailFps | bisos.marmee.aasOutMailFps | bisos.marmee.aasMailFps | bisos.marmee.gmailOauth2 | bisos.marmee.marmeeGmail |
#+end_org """

####+BEGIN: b:py3:cs:framework/csuListProc :pyImports t :csuImports t :csuParams t
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] =Process CSU List= with /11/ in csuList pyImports=t csuImports=t csuParams=t
#+end_org """

from bisos.b.cs import ro
from blee.csPlayer import bleep
from bisos.bpo import bpo
from bisos.bpo import bpoRunBases
from bisos.b import fpCls
from bisos.b import clsMethod_csu
from bisos.marmee import aasInMailFps
from bisos.marmee import aasOutMailFps
from bisos.marmee import aasMailFps
from bisos.marmee import gmailOauth2
from bisos.marmee import marmeeGmail
from bisos.marmee import marmeeQmail


csuList = [ 'bisos.b.cs.ro', 'blee.csPlayer.bleep', 'bisos.bpo.bpo', 'bisos.bpo.bpoRunBases', 'bisos.b.fpCls', 'bisos.b.clsMethod_csu', 'bisos.marmee.aasInMailFps', 'bisos.marmee.aasOutMailFps', 'bisos.marmee.aasMailFps', 'bisos.marmee.gmailOauth2', 'bisos.marmee.marmeeGmail', ]

g_importedCmndsModules = cs.csuList_importedModules(csuList)

def g_extraParams():
    csParams = cs.param.CmndParamDict()
    cs.csuList_commonParamsSpecify(csuList, csParams)
    cs.argsparseBasedOnCsParams(csParams)

####+END:

####+BEGIN: b:py3:cs:main/exposedSymbols :classes ("aasInMailFps.AasInMail_FPs" "aasOutMailFps.AasOutMail_FPs" "aasMailFps.AasMail_FPs")
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~Exposed Symbols List Specification~ with /3/ in Classes List
#+end_org """

AasInMail_FPs = aasInMailFps.AasInMail_FPs # exec/eval-ed as __main__.ClassName
AasOutMail_FPs = aasOutMailFps.AasOutMail_FPs # exec/eval-ed as __main__.ClassName
AasMail_FPs = aasMailFps.AasMail_FPs # exec/eval-ed as __main__.ClassName

####+END:


####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "CmndSvc-s" :extraInfo "class someCommand(cs.Cmnd)"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *CmndSvc-s:* |]]  class someCommand(cs.Cmnd)  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples" :cmndType ""  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples>>  *FrameWrk: ICM Examples*  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """FrameWrk: ICM Examples"""
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org *
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Conventional top level example.
        #+end_org """)

####+BEGIN: b:py3:cs:module/cur_paramsAssign  :curParsList ("aasMarmee_base" "aasMarmee_bpoId" "aasMarmee_svcInMail" "aasMarmee_svcOutMail" "aasMarmee_svcProvider" "aasMarmee_svcInstance" "aasMarmee_envRelPath")
        """ #+begin_org
***  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Currents   [[elisp:(outline-show-subtree+toggle)][||]] ~cur_examples~ (aasMarmee_base aasMarmee_bpoId aasMarmee_svcInMail aasMarmee_svcOutMail aasMarmee_svcProvider aasMarmee_svcInstance aasMarmee_envRelPath)
        #+end_org """
        _parNamesList = [ 'aasMarmee_base', 'aasMarmee_bpoId', 'aasMarmee_svcInMail', 'aasMarmee_svcOutMail', 'aasMarmee_svcProvider', 'aasMarmee_svcInstance', 'aasMarmee_envRelPath',]
        if not (curParsDictValue := currentsConfig.curParsGetAsDictValue_wOp(_parNamesList, outcome=cmndOutcome).results): return(cmndOutcome)
        cur_aasMarmee_base = curParsDictValue['aasMarmee_base']
        cur_aasMarmee_bpoId = curParsDictValue['aasMarmee_bpoId']
        cur_aasMarmee_svcInMail = curParsDictValue['aasMarmee_svcInMail']
        cur_aasMarmee_svcOutMail = curParsDictValue['aasMarmee_svcOutMail']
        cur_aasMarmee_svcProvider = curParsDictValue['aasMarmee_svcProvider']
        cur_aasMarmee_svcInstance = curParsDictValue['aasMarmee_svcInstance']
        cur_aasMarmee_envRelPath = curParsDictValue['aasMarmee_envRelPath']
        def cur_examples():
            cs.examples.execInsert(execLine='bx-currents.cs')
            cs.examples.execInsert(execLine='bx-currents.cs -i usgCursParsGet')
            for each in _parNamesList:
                cs.examples.execInsert(execLine=f'bx-currents.cs -v 20 -i usgCursParsSet {each}={curParsDictValue[each]}')
####+END:

        def cpsInit(): return collections.OrderedDict()
        def menuItem(): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little') # type: ignore
        def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

        #logControler = b_io.log.Control()
        #logControler.loggerSetLevel(20)

        cs.examples.myName(cs.G.icmMyName(), cs.G.icmMyFullName())

        cs.examples.commonBrief()

        bleep.examples_icmBasic()

        cs.examples.menuChapter('*Currents Examples Settings*')
        cur_examples()

        #  RunBases Examples
        bpoRunBases.examples_bpo_runBases(cur_aasMarmee_bpoId, None, sectionTitle="default")
        cur_marmeeEnvRelPath = f"aas/marmee/{cur_aasMarmee_svcProvider}/{cur_aasMarmee_svcInstance}"
        bpoRunBases.examples_bpo_runBases(cur_aasMarmee_bpoId, cur_marmeeEnvRelPath)

        # marmeeCurrentsLib.examples_currents()  # NOTYET 2022, is there anything useful there

####+BEGIN: bx:cs:python:cmnd:subSection :title "marmeAcctsLib Examples"

####+END:

        aasMailFps.examples_csu(cur_aasMarmee_bpoId, cur_marmeeEnvRelPath, sectionTitle="default")

        aasOutMailFps.examples_csu(cur_aasMarmee_bpoId, cur_marmeeEnvRelPath, sectionTitle="default")

        aasInMailFps.examples_csu(cur_aasMarmee_bpoId, cur_marmeeEnvRelPath, sectionTitle="default")

        marmeeGmail.examples_csu(cur_aasMarmee_base, sectionTitle="default")

        marmeeQmail.examplesAas_csu(cur_aasMarmee_base, sectionTitle="default")

        b.niche.examplesNicheRun("usageEnvs")

        return(cmndOutcome)

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Main" :anchor ""  :extraInfo "Framework Dblock"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Main_: |]]  Framework Dblock  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/main :csInfo "csInfo" :noCmndEntry "examples" :extraParamsHook "g_extraParams" :importedCmndsModules "g_importedCmndsModules"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] =g_csMain= (csInfo, _examples_, g_extraParams, g_importedCmndsModules)
#+end_org """

if __name__ == '__main__':
    cs.main.g_csMain(
        csInfo=csInfo,
        noCmndEntry=examples,  # specify a Cmnd name
        extraParamsHook=g_extraParams,
        importedCmndsModules=g_importedCmndsModules,
    )

####+END:

####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:

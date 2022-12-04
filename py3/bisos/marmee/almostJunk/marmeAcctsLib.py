# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Lib= with ICM Cmnds to support managment of Marme related mail profiles
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, b-lib, pyLibPure
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
** This File: /bisos/git/auth/bxRepos/bisos-pip/crypt/py3/bisos/crypt/gpgSym.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['gpgSym'], }
csInfo['version'] = '202209261325'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'gpgSym-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos.crypt/_nodeBase_/fullUsagePanel-en.org][PyFwrk bisos.crypt Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with blee3
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
** Imports Based On Classification=cs-lib
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

####+END:

import os
import collections
#import enum

from unisos.common import icmsPkgLib   # NOTYET, Uses ICM

from bisos.marmee import marmePkgThis

from bisos.common import serviceObject  # NOTYET, Uses ICM
from bisos.currents import currentsConfig

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "marmeAcctsLib_libOverview" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<marmeAcctsLib_libOverview>>  =verify= argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class marmeAcctsLib_libOverview(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:

        moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
This module is part of BISOS and its primary documentation is in  http://www.by-star.net/PLPC/180047
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]     ICMs Pkg Inputs And Configuration Patterns                 :Overview:

    The following modules work collaboratively
     + icmNamePkgThis.py            :: this module which is the main interface for the pkg
     + icmNamePkgConfig.py          :: the file that locates config and data dirs
     + unisos.common.icmsPkgLib.py  :: the lib that implements icmPkg polices

    An ICM-Pkg typically has the following accompanying directories:
     - icmName-config     :: Where fp params for the pkg are (Read/Write)
     - icmName-base       :: Where data and inputs are (Read only)
     - pkgControl         :: bxoIdSr params that control Instance Execution

***   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]   General Execution Configuration Vs Instance Execution Configuration

    Execution configuration is performed in 2 layers:

    1) General Execution  Parameters  :: These are specified in icmName- dir
         1.1) icmName-config
         1.2) icmName-base

    2) Instance Execution Configuration Parameters :: These are specified in control base

***   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]   Organization Of icmNamePkgConfig.py

    The organization of icmNamePkgConfig.py usually follows the pattern below:
    
      * Interface to obtain 
        ** icmName-config -- configBaseDirGet
        ** icmName-base  -- inputsBaseDirGet

      * Interface to obtain icmPkg General Execution params
        ** control
        ** var
        ** tmp
        ** log

      * Interface to obtain icmPkg Instance Execution params
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** DONE [[elisp:(org-cycle)][| ]]  Current         :: [2018-05-30 Wed] BxoIdSr Updates and cleanups completed  [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        icm.unusedSuppressForEval(moduleUsage, moduleStatus)
        actions = self.cmndArgsGet("0&2", cmndArgsSpecDict, argsList)
        if actions[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            actions = argChoices
        for each in actions:
            print(each)
            if rtInv.outs:
                #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                #version(interactive=True)
                exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="actions",
            argDefault='all',
            argChoices=['all', 'moduleDescription', 'moduleUsage', 'moduleStatus'],
            argDescription="Output relevant information",
        )

        return cmndArgsSpecDict
####+END:

####+BEGIN: bx:cs:python:section :title "Common Module Conventions (BxoIdSr)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Module Conventions (BxoIdSr)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGINNOT: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/curGetBxOSr.py"
""" #+begin_org
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-BxoIdSr   :: /curGet_{bxoId,sr}/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """

def curGet_bxoId(): return currentsConfig.bxoId_fpObtain(configBaseDir=None)
def curGet_sr(): return currentsConfig.sr_fpObtain(configBaseDir=None)
def cmndParsCurBxoSr(cps): cps['bxoId'] = curGet_bxoId(); cps['sr'] = curGet_sr()
####+END:

####+BEGIN: bx:cs:python:section :title "Obtain ICM-Package Anchor For General Execution"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Obtain ICM-Package Anchor For General Execution*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGIN: bx:cs:python:func :funcName "pkgAnchor_configDir_obtain" :funcType "anyOrNone" :retType "str(path)" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /pkgAnchor_configDir_obtain/ retType=str(path) argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def pkgAnchor_configDir_obtain():
####+END:
    return marmePkgThis.pkgBase_configDir()


####+BEGIN: bx:cs:python:func :funcName "pkgAnchor_baseDir_obtain" :funcType "anyOrNone" :retType "str(path)" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /pkgAnchor_baseDir_obtain/ retType=str(path) argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def pkgAnchor_baseDir_obtain():
####+END:
    return (
            marmePkgThis.pkgBase_baseDir()
    )


####+BEGIN: bx:cs:python:func :funcName "inputsBaseDirGet" :funcType "anyOrNone" :retType "str(path)" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /inputsBaseDirGet/ retType=str(path) argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def inputsBaseDirGet():
####+END:
    return (
        icmsPkgLib.pkgInputsBaseDir_obtain(
            pkgAnchor_baseDir_obtain()
        )
    )


####+BEGIN: bx:cs:python:section :title "Obtain ICM-Package Canonical General Execution Bases"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Obtain ICM-Package Canonical General Execution Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:cs:python:func :funcName "mailAcctsBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /mailAcctsBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def mailAcctsBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        icmsPkgLib.pkgBaseDir_obtain(bxoId=bxoId, sr=sr,)
    )



####+BEGIN: bx:cs:python:func :funcName "configBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /configBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def configBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        os.path.join(
            icmsPkgLib.varConfigBaseDir_obtain(
                icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
                bxoId=bxoId,
                sr=sr,
            ),
            "marme"   # NOTYET -- icmsPkgName
        )
    )



####+BEGIN: bx:cs:python:func :funcName "controlBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /controlBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def controlBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    retVal = icmsPkgLib.controlBaseDir_obtain(
        icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
        bxoId=bxoId,
        sr=sr,
    )

    return (
        os.path.join(
            retVal,
            "control",
        )
    )


####+BEGIN: bx:cs:python:func :funcName "varBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /varBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def varBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        os.path.join(
            icmsPkgLib.varBaseDir_obtain(
                icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
                bxoId=bxoId,
                sr=sr,            
            ),
            "marme"   # NOTYET -- icmsPkgName
        )
    )

    
####+BEGIN: bx:cs:python:func :funcName "tmpBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /tmpBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def tmpBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        icmsPkgLib.tmpBaseDir_obtain(
            icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
            bxoId=bxoId,
            sr=sr,
        )
    )

    
####+BEGIN: bx:cs:python:func :funcName "logBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /logBaseDirGet/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def logBaseDirGet(
    bxoId=None,
    sr=None,
):
####+END:
    return(
        icmsPkgLib.logBaseDir_obtain(
            icmsPkgInfoBaseDir=pkgAnchor_configDir_obtain(),
            bxoId=bxoId,
            sr=sr,
        )
    )


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Control From  FP Obtain*
"""

    
####+BEGIN: bx:cs:python:func :funcName "enabledControlProfileObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /enabledControlProfileObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def enabledControlProfileObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """Returns as a string fp value read."""
    return b.fp.FileParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledControlProfile",
    )

####+BEGIN: bx:cs:python:func :funcName "availableControlProfilesObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /availableControlProfilesObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def availableControlProfilesObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
Returns a list
"""
    availablesList = list()
    controlBaseDir = controlBaseDirGet(bxoId=bxoId, sr=sr,)
    for each in  os.listdir(controlBaseDir):
        if each == "CVS":
            continue
        if each == "common":
            continue
        eachFullPath = os.path.join(controlBaseDir, each)
        if not os.path.isdir(eachFullPath):
            continue
        availablesList.append(each)
    return availablesList

####+BEGIN: bx:cs:python:func :funcName "enabledInMailAcctObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /enabledInMailAcctObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def enabledInMailAcctObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
** Called obtain to leave Get for the IIF"""
    return b.fp.FileParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledInMailAcct",          
    )

####+BEGIN: bx:cs:python:func :funcName "availableInMailAcctObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /availableInMailAcctObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def availableInMailAcctObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
Returns a list
"""
    availablesList = list()
    baseDir = os.path.join(
           controlProfileBaseDirGet(
               enabledControlProfileObtain(bxoId=bxoId, sr=sr,),
               bxoId=bxoId,
               sr=sr,
           ),
            "inMail",
    )

    for each in  os.listdir(baseDir):
        if each == "CVS":
            continue
        if each == "common":
            continue
        eachFullPath = os.path.join(baseDir, each)
        if not os.path.isdir(eachFullPath):
            continue
        availablesList.append(each)
    return availablesList

####+BEGIN: bx:cs:python:func :funcName "enabledOutMailAcctObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /enabledOutMailAcctObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def enabledOutMailAcctObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
** Called obtain to leave Get for the IIF"""
    return b.fp.FileParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledOutMailAcct",          
    )

####+BEGIN: bx:cs:python:func :funcName "availableOutMailAcctObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /availableOutMailAcctObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def availableOutMailAcctObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
Returns a list
"""
    availablesList = list()
    baseDir = os.path.join(
        controlProfileBaseDirGet(
            enabledControlProfileObtain(bxoId=bxoId, sr=sr,),
            bxoId=bxoId,
            sr=sr,
        ),
        "outMail",
    )

    for each in  os.listdir(baseDir):
        if each == "CVS":
            continue
        if each == "common":
            continue
        eachFullPath = os.path.join(baseDir, each)
        if not os.path.isdir(eachFullPath):
            continue
        availablesList.append(each)
    return availablesList


####+BEGIN: bx:cs:python:func :funcName "enabledMailBoxObtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /enabledMailBoxObtain/ retType=bool argsList=(bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def enabledMailBoxObtain(
    bxoId=None,
    sr=None,
):
####+END:
    """
** Called obtain to leave Get for the IIF"""
    return b.fp.FileParamValueReadFrom(
        parRoot=os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            "common",
            "selections",
            "fp",
        ),
        parName="enabledMailBox",          
    )


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Control Base Directory From FP Get*
"""

####+BEGIN: bx:cs:python:func :funcName "controlProfileBaseDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /controlProfileBaseDirGet/ retType=bool argsList=(controlProfile bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def controlProfileBaseDirGet(
    controlProfile,
    bxoId=None,
    sr=None,
):
####+END:
    """
** Joins controlBaseDirGet() and enabledControlProfileObtain()
"""
    if not controlProfile:
        controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)

    return os.path.abspath(
        os.path.join(
            controlBaseDirGet(bxoId=bxoId, sr=sr,),
            controlProfile,
    ))



####+BEGIN: bx:cs:python:func :funcName "outMailAcctDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile outMailAcct bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /outMailAcctDirGet/ retType=bool argsList=(controlProfile outMailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def outMailAcctDirGet(
    controlProfile,
    outMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    return os.path.abspath(
        os.path.join(
           controlProfileBaseDirGet(controlProfile, bxoId=bxoId, sr=sr,),
            "outMail",
            outMailAcct,
            "fp",
    ))


####+BEGIN: bx:cs:python:func :funcName "outMailCommonDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /outMailCommonDirGet/ retType=bool argsList=(controlProfile bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def outMailCommonDirGet(
    controlProfile,
    bxoId=None,
    sr=None,
):
####+END:
    if not controlProfile:
        controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)
    return os.path.abspath(
        os.path.join(
            controlProfileBaseDirGet(controlProfile, bxoId=bxoId, sr=sr,),
            "outMail",
            "common",
            #"fp",         # NOTYET, Needs to be revisited
    ))

####+BEGIN: bx:cs:python:func :funcName "inMailAcctDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile inMailAcct bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /inMailAcctDirGet/ retType=bool argsList=(controlProfile inMailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def inMailAcctDirGet(
    controlProfile,
    inMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    if not controlProfile:
        controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)
    return os.path.abspath(
        os.path.join(
            controlProfileBaseDirGet(controlProfile, bxoId=bxoId, sr=sr,),             
            "inMail",
            inMailAcct,
            "fp",
    ))

####+BEGIN: bx:cs:python:func :funcName "inMailCommonDirGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /inMailCommonDirGet/ retType=bool argsList=(controlProfile bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def inMailCommonDirGet(
    controlProfile,
    bxoId=None,
    sr=None,
):
####+END:
    if not controlProfile:
        controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)
    return (
        os.path.abspath(
            os.path.join(
                controlProfileBaseDirGet(controlProfile, bxoId=bxoId, sr=sr,),
                "inMail"
                "common"
                "fp"            
            )))


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *VAR Base Directory Get*
"""

####+BEGIN: bx:cs:python:func :funcName "getPathForAcctMaildir" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile mailAcct bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /getPathForAcctMaildir/ retType=bool argsList=(controlProfile mailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def getPathForAcctMaildir(
    controlProfile,
    mailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    """
** NOTYET, controlProfile is not being used.
"""
    return (
        os.path.join(
            varBaseDirGet(bxoId=bxoId, sr=sr,),
            "inMail",
            controlProfile,
            mailAcct,
            "maildir"
        ))

####+BEGIN: bx:cs:python:func :funcName "getPathForAcctMbox" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile mailAcct mbox bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /getPathForAcctMbox/ retType=bool argsList=(controlProfile mailAcct mbox bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def getPathForAcctMbox(
    controlProfile,
    mailAcct,
    mbox,
    bxoId=None,
    sr=None,
):
####+END:
    #if not controlProfile:
        #controlProfile = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)

    if not mailAcct:
        mailAcct = enabledInMailAcctObtain(bxoId=bxoId, sr=sr,)

    if not mbox:
        mbox = enabledMailBoxObtain(bxoId=bxoId, sr=sr,)

    return (
        os.path.join(
            varBaseDirGet(bxoId=bxoId, sr=sr,),
            "inMail",
            controlProfile,            
            mailAcct,
            "maildir",
            mbox,
        ))

####+BEGIN: bx:cs:python:func :funcName "getPathForInMailConfig" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile inMailAcct bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /getPathForInMailConfig/ retType=bool argsList=(controlProfile inMailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def getPathForInMailConfig(
    controlProfile,
    inMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    return (
        os.path.join(
            configBaseDirGet(bxoId=bxoId, sr=sr,),
            "inMail",
            controlProfile,            
            inMailAcct,
        ))

####+BEGIN: bx:cs:python:func :funcName "getPathForOutMailConfig" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile outMailAcct bxoId=None sr=None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /getPathForOutMailConfig/ retType=bool argsList=(controlProfile outMailAcct bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
#+end_org """
def getPathForOutMailConfig(
    controlProfile,
    outMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    return (
        os.path.join(
            configBaseDirGet(bxoId=bxoId, sr=sr,),
            "outMail",
            controlProfile,            
            outMailAcct,
        ))


####+BEGIN: bx:cs:python:subSection :title "Common Arguments Specification"

####+END:

####+BEGIN: bx:cs:python:func :funcName "commonParamsSpecify" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "csParams"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/ retType=bool argsList=(csParams)  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
    csParams,
):
####+END:
    
    enabledControlProfile = enabledControlProfileObtain(curGet_bxoId(), curGet_sr())    
    enabledInMailAcct = enabledInMailAcctObtain(curGet_bxoId(), curGet_sr())
    enabledOutMailAcct = enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr())        

    csParams.parDictAdd(
        parName='controlProfile',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault="{default}".format(default=enabledControlProfile),
        parChoices=["someOptionalPar", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--controlProfile',
    )

    csParams.parDictAdd(
        parName='inMailAcct',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault="{default}".format(default=enabledInMailAcct),
        parChoices=["someOptionalPar", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--inMailAcct',
    )
    
    csParams.parDictAdd(
        parName='outMailAcct',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault="{default}".format(default=enabledOutMailAcct),
        parChoices=["someOptionalPar", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--outMailAcct',
    )
    
    csParams.parDictAdd(
        parName='firstName',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--firstName',
    )
    
    csParams.parDictAdd(
        parName='lastName',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--lastName',
    )

    csParams.parDictAdd(
        parName='userName',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--userName',
    )

    csParams.parDictAdd(
        parName='userPasswd',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--userPasswd',
    )
    
    csParams.parDictAdd(
        parName='mtaRemHost',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--mtaRemHost',
    )

    csParams.parDictAdd(
        parName='mtaRemProtocol',
        parDescription="Base for Domain/Site/Source of incoming Mail",
        parDataType=None,
        parDefault=None,
        parChoices=["someOptionalPar", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--mtaRemProtocol',
    )
    
    
    # csParams.parDictAdd(
    #     parName='imapServer',
    #     parDescription="Base for Domain/Site/Source of incoming Mail",
    #     parDataType=None,
    #     parDefault=None,
    #     parChoices=["someOptionalPar", "UserInput"],
    #     parScope=cs.CmndParamScope.TargetParam,
    #     argparseShortOpt=None,
    #     argparseLongOpt='--imapServer',
    # )

    csParams.parDictAdd(
        parName='inMailAcctMboxesPath',
        parDescription="Base Directory Of Maildir where msgs are retrieved to.",
        parDataType=None,
        parDefault=None,        
        #parDefault="../var/inMail/{default}/maildir/".format(default=enabledMailAcct),
        parChoices=["someFile", "UserInput"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--inMailAcctMboxesPath',
    )
    
    csParams.parDictAdd(
        parName='inMbox',
        parDescription="Name of MailBox to be joined with inMailAcctMboxesPath.",
        parDataType=None,
        parDefault=None,
        parChoices=["envelope", "Tmp"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--inMbox',
    )

    csParams.parDictAdd(
        parName='mboxesList',
        parDescription="Name of MailBox to be joined with inMailAcctMboxesPath.",
        parDataType=None,
        parDefault=None,
        parChoices=["envelope", "Tmp"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--mboxesList',
    )

    csParams.parDictAdd(
        parName='ssl',
        parDescription="Name of MailBox to be joined with inMailAcctMboxesPath.",
        parDataType=None,
        parDefault=None,
        parChoices=["no", "on"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--ssl',
    )
    
    csParams.parDictAdd(
        parName='sendingMethod',
        parDescription="sending method for outgoing email",
        parDataType=None,
        parDefault=None,
        parChoices=["inject", "authSmtp"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--sendingMethod',
    )

    csParams.parDictAdd(
        parName='envelopeAddr',
        parDescription="Envelope Address Of Outgoing Email",
        parDataType=None,
        parDefault=None,
        parChoices=["envelop@example.com"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--envelopeAddr',
    )

    # csParams.parDictAdd(
    #     parName='parGroup',
    #     parDescription="Temporary till args dblock processing gets fixed",
    #     parDataType=None,
    #     parDefault=None,
    #     parChoices=["access", ],
    #     parScope=cs.CmndParamScope.TargetParam,
    #     argparseShortOpt=None,
    #     argparseLongOpt='--parGroup',
    # )

    serviceObject.commonParamsSpecify(csParams)

    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Common Examples Sections*
"""

####+BEGIN: bx:cs:python:func :funcName "examples_bxoSrPkgInfoParsGet" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_bxoSrPkgInfoParsGet/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_bxoSrPkgInfoParsGet():
####+END:
    """."""
    
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)
    
    cs.examples.menuChapter('* =Info=  BxoSr PkgInfoParsGet*')

    cmndName = "bxoSrPkgInfoParsGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cmndName = "bxoSrPkgInfoMkdirs" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps);
    menuItem(verbosity='none') ; menuItem(verbosity='little')
    
    return

####+BEGIN: bx:cs:python:func :funcName "examples_controlProfileManage" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_controlProfileManage/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_controlProfileManage():
####+END:
    """.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)
    
    cs.examples.menuChapter('* =Selection=  Control Profiles -- /{}/ --*'.format(
        enabledControlProfileObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "enabledControlProfileGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cmndName = "enabledControlProfileSet"

    for each in availableControlProfilesObtain(curGet_bxoId(), curGet_sr()):
        cmndArgs = " {controlProfile}".format(controlProfile=each)
        cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='little')

    return


####+BEGIN: bx:cs:python:func :funcName "examples_enabledInMailAcctConfig" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_enabledInMailAcctConfig/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_enabledInMailAcctConfig():
####+END:
    """
** Select Enabled Mail Account Config. Read/Writeen to control/common/selections/fp
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)
 
    cs.examples.menuChapter('* =Selection=  InMailAccts -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )

    cmndName = "enabledInMailAcctGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cmndName = "enabledInMailAcctSet"

    for each in availableInMailAcctObtain(curGet_bxoId(), curGet_sr()):
        cmndArgs = " {}".format(each)
        cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='little')        

    return

####+BEGIN: bx:cs:python:func :funcName "examples_enabledOutMailAcctConfig" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_enabledOutMailAcctConfig/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_enabledOutMailAcctConfig():
####+END:
    """
** Select Enabled Mail Account Config. Read/Writeen to control/common/selections/fp
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    cs.examples.menuChapter('* =Selection=  OutMailAccts -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr())))

    cmndName = "enabledOutMailAcctGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cmndName = "enabledOutMailAcctSet"    

    for each in availableOutMailAcctObtain(curGet_bxoId(), curGet_sr()):
        cmndArgs = " {}".format(each)
        cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='little')        

    return
    
####+BEGIN: bx:cs:python:func :funcName "examples_select_mailBox" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_select_mailBox/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_select_mailBox():
####+END:
    """."""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    cs.examples.menuChapter('* =Selection=  MailBox -- /{controlProfile}+{mailAcct}+{mBox}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()),
        mBox=enabledMailBoxGet().cmnd(bxoId=curGet_bxoId(), sr=curGet_sr()).results,
        )
    )

    cmndName = "enabledMailBoxGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cmndName = "enabledMailBoxSet" ; cmndArgs = "Inbox"
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')
    
    
    
####+BEGIN: bx:cs:python:func :funcName "examples_inMailAcctAccessPars" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_inMailAcctAccessPars/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_inMailAcctAccessPars():
####+END:
    """
** Auxiliary examples to be commonly used.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)
    
    cs.examples.menuChapter('* =FP Values=  inMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctParsGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    menuLine = """"""
    icm.cmndExampleMenuItem(menuLine, icmName="marmeAcctsManage.py", verbosity='none')
    

####+BEGIN: bx:cs:python:func :funcName "examples_inMailAcctAccessParsFull" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_inMailAcctAccessParsFull/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_inMailAcctAccessParsFull():
####+END:
    """
** Auxiliary examples to be commonly used.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)
    
    cs.examples.menuChapter('* =FP Values=  inMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctParsGet" ; cmndArgs = ""
    cps=cpsInit(); cmndParsCurBxoSr(cps); menuItem(verbosity='none')

    cs.examples.menuSection('*inMail /Access/ ParsSet -- /defaulMailAcct={}/ --*'.format(
        enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctAccessParsSet" ; cmndArgs = "" ;
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    cps['userName'] = "UserName" ; cps['userPasswd'] = "UserPasswd" ; cps['imapServer'] = "ImapServer"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="echo", icmName=None)
    
    cs.examples.menuSection('*inMail /ControllerInfo/ ParsSet -- /defaulMailAcct={}/ --*'.format(
        enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctControllerInfoParsSet" ; cmndArgs = "" 
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    cps['firstName'] = "FirstName" ; cps['lastName'] = "LastName"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="echo", icmName=None)
    
    cs.examples.menuSection('*inMail /Retrieval/ ParsSet -- /defaulMailAcct={}/ --*'.format(
        enabledInMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "inMailAcctRetrievalParsSet" ; cmndArgs = "" 
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    cps['inMailAcctMboxesPath'] = "MaildirPath"; cps['mboxesList'] = ""; cps['ssl'] = "on"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="echo", icmName=None)

    cmndName = "inMailAcctRetrievalParsSet" ; cmndArgs = "" 
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    mailDirPath = getPathForAcctMaildir(
        enabledControlProfileObtain(
            curGet_bxoId(),
            curGet_sr()
        ),
        enabledInMailAcctObtain(
            curGet_bxoId(),
            curGet_sr()
        ),
        bxoId=curGet_bxoId(),
        sr=curGet_sr(),
    )
    cps['inMailAcctMboxesPath'] = mailDirPath
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="", icmName=None)

    cmndName = "inMailAcctRetrievalParsSet" ; cmndArgs = "" 
    cps=cpsInit() ; cmndParsCurBxoSr(cps)
    cps['mboxesList'] = "Inbox"; cps['ssl'] = "on"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper="echo", icmName=None)
    
    
####+BEGIN: bx:cs:python:func :funcName "examples_outMailAcctAccessPars" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_outMailAcctAccessPars/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_outMailAcctAccessPars():
####+END:
    """.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    cs.examples.menuChapter('* =FP Values=  outMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "outMailAcctParsGet" ; cmndArgs = "" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none')

    menuLine = """"""
    icm.cmndExampleMenuItem(menuLine, icmName="marmeAcctsManage.py", verbosity='none')    

    
####+BEGIN: bx:cs:python:func :funcName "examples_outMailAcctAccessParsFull" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_outMailAcctAccessParsFull/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_outMailAcctAccessParsFull():
####+END:
    """.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    cs.examples.menuChapter('* =FP Values=  outMail Controls -- /{controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )
    cmndName = "outMailAcctParsGet" ; cmndArgs = "" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none')

    cs.examples.menuSection('*outMail /Access/ ParsSet -- /enabledMailAcct={controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )

    cmndName = "outMailAcctParsSet" ; cmndArgs = "access" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)
    cps['userName']="TBS" ; cps['userPasswd']="TBS" ; cps['mtaRemHost']="TBS" ; cps['mtaRemProtocol']="smtp_ssl/smtp_tls/smtp"     
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='none')

    cs.examples.menuSection('*outMail /ControllerInfo/ ParsSet -- /enabledMailAcct={controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )

    cmndName = "outMailAcctParsSet" ; cmndArgs = "controllerInfo" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)    
    cps['firstName']="TBS" ; cps['lastName']="TBS"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='none')

    cs.examples.menuSection('*outMail /Submission/ ParsSet -- /enabledMailAcct={controlProfile}+{mailAcct}/ --*'.format(
        controlProfile=enabledControlProfileObtain(curGet_bxoId(), curGet_sr()),
        mailAcct=enabledOutMailAcctObtain(curGet_bxoId(), curGet_sr()))
    )

    cmndName = "outMailAcctParsSet" ; cmndArgs = "submission" ; cps = collections.OrderedDict()
    cmndParsCurBxoSr(cps)    
    cps['sendingMethod']="inject/submit" ; cps['envelopeAddr']="TBS"
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='none')

    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *File Parameters Get/Set -- Commands*
"""

####+BEGIN: bx:cs:python:func :funcName "FP_readTreeAtBaseDir_CmndOutput" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "interactive fpBaseDir cmndOutcome"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /FP_readTreeAtBaseDir_CmndOutput/ retType=bool argsList=(interactive fpBaseDir cmndOutcome)  [[elisp:(org-cycle)][| ]]
#+end_org """
def FP_readTreeAtBaseDir_CmndOutput(
    interactive,
    fpBaseDir,
    cmndOutcome,
):
####+END:
    """Invokes FP_readTreeAtBaseDir.cmnd as interactive-output only."""
    #
    # Interactive-Output + Chained-Outcome Command Invokation
    #
    FP_readTreeAtBaseDir = icm.FP_readTreeAtBaseDir()
    FP_readTreeAtBaseDir.cmndLineInputOverRide = True
    FP_readTreeAtBaseDir.cmndOutcome = cmndOutcome
        
    return FP_readTreeAtBaseDir.cmnd(
        interactive=interactive,
        FPsDir=fpBaseDir,
    )



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bxoSrPkgInfoMkdirs" :comment "" :parsMand "bxoId sr" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bxoSrPkgInfoMkdirs>>  =verify= parsMand=bxoId sr ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bxoSrPkgInfoMkdirs(cs.Cmnd):
    cmndParamsMandatory = [ 'bxoId', 'sr', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Mandatory Param
             sr: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:

        outcome = icm.subProc_bash("""\
mkdir -p  {}"""
                                   .format(controlBaseDirGet(bxoId=bxoId, sr=sr))
        ).log()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        outcome = icm.subProc_bash("""\
mkdir -p {}"""
                                   .format(varBaseDirGet(bxoId=bxoId, sr=sr))
        ).log()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        outcome = icm.subProc_bash("""\
mkdir -p {}"""
                                   .format(configBaseDirGet(bxoId=bxoId, sr=sr))
        ).log()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))
        
        outcome = icm.subProc_bash("""\
mkdir -p {}"""
                                   .format(tmpBaseDirGet(bxoId=bxoId, sr=sr))
        ).log()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))
        
        outcome = icm.subProc_bash("""\
mkdir -p {}"""
                                   .format(logBaseDirGet(bxoId=bxoId, sr=sr))
        ).log()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))
        
        
        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bxoSrPkgInfoParsGet" :comment "" :parsMand "bxoId sr" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bxoSrPkgInfoParsGet>>  =verify= parsMand=bxoId sr ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bxoSrPkgInfoParsGet(cs.Cmnd):
    cmndParamsMandatory = [ 'bxoId', 'sr', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Mandatory Param
             sr: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
 
        if rtInv.outs:
            b_io.ann.write("controlBaseDir={}".format(
                controlBaseDirGet(bxoId=bxoId, sr=sr)
            ))
            b_io.ann.write("varBaseDir={}".format(
                varBaseDirGet(bxoId=bxoId, sr=sr)
            ))
            b_io.ann.write("configBaseDir={}".format(
                configBaseDirGet(bxoId=bxoId, sr=sr)
            ))
            b_io.ann.write("tmpBaseDir={}".format(
                tmpBaseDirGet(bxoId=bxoId, sr=sr)
            ))
            b_io.ann.write("logBaseDir={}".format(
                logBaseDirGet(bxoId=bxoId, sr=sr)
            ))


        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "enabledControlProfileGet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<enabledControlProfileGet>>  =verify= parsOpt=bxoId sr ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class enabledControlProfileGet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        """Output the current from -- NOTYET -- Should write at {varBase}/selections/fp"""
        enabledMailAcct = enabledControlProfileObtain(bxoId=bxoId, sr=sr,)
 
        if rtInv.outs:
            b_io.ann.write(enabledMailAcct)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=enabledMailAcct,
        )

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "enabledControlProfileSet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<enabledControlProfileSet>>  =verify= parsOpt=bxoId sr argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class enabledControlProfileSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Write as a FP the enabledControlProfile.
"""

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(bxoId=bxoId, sr=sr,),   # NOTYET
                    "common",
                    "selections",
                    "fp",
                    "enabledControlProfile",
                ),
                parValue=each,
            )

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=each,
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "enabledInMailAcctGet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<enabledInMailAcctGet>>  =verify= parsOpt=bxoId sr ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class enabledInMailAcctGet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
    
        enabledInMailAcct = enabledInMailAcctObtain(bxoId=bxoId, sr=sr,)  # NOTYET
 
        if rtInv.outs:
            b_io.ann.write(enabledInMailAcct)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=enabledInMailAcct,
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "enabledInMailAcctSet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<enabledInMailAcctSet>>  =verify= parsOpt=bxoId sr argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class enabledInMailAcctSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        """
** Write as a FP  the enabledMailAcct.
"""

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(bxoId=bxoId, sr=sr,),   # NOTYET
                    "common",
                    "selections",
                    "fp",
                    "enabledInMailAcct",
                ),
                parValue=each,
            )

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=each,
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "enabledOutMailAcctGet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<enabledOutMailAcctGet>>  =verify= parsOpt=bxoId sr ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class enabledOutMailAcctGet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        """
** Output the current enabledMailAcct
    """
    
        enabledOutMailAcct = enabledOutMailAcctObtain(bxoId=bxoId, sr=sr,)  # NOTYET
 
        if rtInv.outs:
            b_io.ann.write(enabledOutMailAcct)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=enabledOutMailAcct,
        )



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "enabledOutMailAcctSet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<enabledOutMailAcctSet>>  =verify= parsOpt=bxoId sr argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class enabledOutMailAcctSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        """
** Write as a FP  the enabledMailAcct.
"""

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(bxoId=bxoId, sr=sr,),  # NOTYET
                    "common",
                    "selections",
                    "fp",
                    "enabledOutMailAcct",
                ),
                parValue=each,
            )

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=each,
        )



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "enabledMailBoxGet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<enabledMailBoxGet>>  =verify= parsOpt=bxoId sr ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class enabledMailBoxGet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        """
** Output the current enabledMailBox
    """
    
        enabledMailBox = enabledMailBoxObtain(bxoId=bxoId, sr=sr,)
 
        if rtInv.outs:
            b_io.ann.write(enabledMailBox)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=enabledMailBox,
        )
    

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "enabledMailBoxSet" :comment "" :parsMand "" :parsOpt "bxoId sr" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<enabledMailBoxSet>>  =verify= parsOpt=bxoId sr argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class enabledMailBoxSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        """
** Write as a FP  the enabledMailBox.
"""

        icmRunArgs = G.icmRunArgsGet()
        for each in icmRunArgs.cmndArgs:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(
                    controlBaseDirGet(bxoId=bxoId, sr=sr,),  # NOTYET
                    "common",
                    "selections",
                    "fp",
                    "enabledMailBox",
                ),
                parValue=each,
            )

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=each,
        )
    
####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "inMailAcctParsGet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin 0 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<inMailAcctParsGet>>  =verify= parsOpt=bxoId sr controlProfile inMailAcct argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class inMailAcctParsGet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             controlProfile: typing.Optional[str]=None,  # Cs Optional Param
             inMailAcct: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:

        if rtInv.outs:
            parTypes = self.cmndArgsGet("0&2", cmndArgsSpecDict, argsList)
        else:
            parTypes = effectiveArgsList
            
        if parTypes:
            if parTypes[0] == "all":
                    cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
                    argChoices = cmndArgsSpec.argChoicesGet()
                    argChoices.pop(0)
                    parTypes = argChoices

        for each in parTypes:
            fpBaseDir = os.path.join(
                inMailAcctDirGet(controlProfile, inMailAcct, bxoId=bxoId, sr=sr,),
                each,
            )
            b_io.tm.here(
                "controlProfile={controlProfile} -- inMailAcct={inMailAcct} -- fpBaseDir={fpBaseDir}".format(
                    controlProfile=controlProfile, inMailAcct=inMailAcct, fpBaseDir=fpBaseDir,)
            )
            FP_readTreeAtBaseDir_CmndOutput(
                interactive=interactive,
                fpBaseDir=fpBaseDir,
                cmndOutcome=cmndOutcome,
            )

        return cmndOutcome

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="parTypes",
            argDefault="all",               
            argChoices=['all', 'access', 'controllerInfo', 'retrieval'],
            argDescription="Action to be specified by rest"
        )

        return cmndArgsSpecDict
    

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "inMailAcctAccessParsSet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct userName userPasswd imapServer" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<inMailAcctAccessParsSet>>  =verify= parsOpt=bxoId sr controlProfile inMailAcct userName userPasswd imapServer ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class inMailAcctAccessParsSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', 'userName', 'userPasswd', 'imapServer', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             controlProfile: typing.Optional[str]=None,  # Cs Optional Param
             inMailAcct: typing.Optional[str]=None,  # Cs Optional Param
             userName: typing.Optional[str]=None,  # Cs Optional Param
             userPasswd: typing.Optional[str]=None,  # Cs Optional Param
             imapServer: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'userName': userName, 'userPasswd': userPasswd, 'imapServer': imapServer, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:

        inMailAcctDir = os.path.join(
            inMailAcctDirGet(inMailAcct, bxoId=bxoId, sr=sr,),
            "access",
        )

        if userName:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "userName"),
                parValue=userName,
            )

        if userPasswd:            
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "userPasswd"),
                parValue=userPasswd,
            )
            
        if imapServer:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "imapServer"),
                parValue=imapServer,
            )
        
        if rtInv.outs:
            icm.ANN_here(inMailAcctDir)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=inMailAcctDir,
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "inMailAcctControllerInfoParsSet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct firstName lastName" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<inMailAcctControllerInfoParsSet>>  =verify= parsOpt=bxoId sr controlProfile inMailAcct firstName lastName ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class inMailAcctControllerInfoParsSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', 'firstName', 'lastName', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             controlProfile: typing.Optional[str]=None,  # Cs Optional Param
             inMailAcct: typing.Optional[str]=None,  # Cs Optional Param
             firstName: typing.Optional[str]=None,  # Cs Optional Param
             lastName: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'firstName': firstName, 'lastName': lastName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:

        inMailAcctDir = os.path.join(
            inMailAcctDirGet(inMailAcct, bxoId=bxoId, sr=sr,),
            "controllerInfo",
        )

        if firstName:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "firstName"),
                parValue=firstName,
            )

        if lastName:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "lastName"),
                parValue=lastName,
            )
        
        if rtInv.outs:
            icm.ANN_here(inMailAcctDir)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=inMailAcctDir,
        )

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "inMailAcctRetrievalParsSet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct inMailAcctMboxesPath mboxesList ssl" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<inMailAcctRetrievalParsSet>>  =verify= parsOpt=bxoId sr controlProfile inMailAcct inMailAcctMboxesPath mboxesList ssl ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class inMailAcctRetrievalParsSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', 'inMailAcctMboxesPath', 'mboxesList', 'ssl', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             controlProfile: typing.Optional[str]=None,  # Cs Optional Param
             inMailAcct: typing.Optional[str]=None,  # Cs Optional Param
             inMailAcctMboxesPath: typing.Optional[str]=None,  # Cs Optional Param
             mboxesList: typing.Optional[str]=None,  # Cs Optional Param
             ssl: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'inMailAcctMboxesPath': inMailAcctMboxesPath, 'mboxesList': mboxesList, 'ssl': ssl, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:

        inMailAcctDir = os.path.join(
            inMailAcctDirGet(controlProfile, inMailAcct, bxoId=bxoId, sr=sr,),
        "retrieval",
        )

        if inMailAcctMboxesPath: (           
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "inMailAcctMboxesPath"),
                parValue=os.path.abspath(
                    inMailAcctMboxesPath,
                )))

        if mboxesList: (           
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "mboxesList"),
                parValue=mboxesList,
                ))

        if ssl: (
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(inMailAcctDir, "ssl"),
                parValue=ssl,
            ))
            
        if rtInv.outs:
            icm.ANN_here(inMailAcctDir)

        return (
            cmndOutcome.set(
                opError=b.OpError.Success,
                opResults=inMailAcctDir,
            ))


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "outMailAcctParsGet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile outMailAcct" :argsMin 0 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<outMailAcctParsGet>>  =verify= parsOpt=bxoId sr controlProfile outMailAcct argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class outMailAcctParsGet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'outMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             controlProfile: typing.Optional[str]=None,  # Cs Optional Param
             outMailAcct: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'outMailAcct': outMailAcct, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        parTypes = self.cmndArgsGet("0&2", cmndArgsSpecDict, argsList)
        
        if parTypes:
            if parTypes[0] == "all":
                    cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
                    argChoices = cmndArgsSpec.argChoicesGet()
                    argChoices.pop(0)
                    parTypes = argChoices

        for each in parTypes:
            fpBaseDir = os.path.join(
                outMailAcctDirGet(controlProfile, outMailAcct, bxoId=bxoId, sr=sr,),
                each,
            )
            b_io.tm.here(
                "controlProfile={controlProfile} -- outMailAcct={outMailAcct} -- fpBaseDir={fpBaseDir}".format(
                    controlProfile=controlProfile, outMailAcct=outMailAcct, fpBaseDir=fpBaseDir,)
            )
            FP_readTreeAtBaseDir_CmndOutput(
                interactive=interactive,
                fpBaseDir=fpBaseDir,
                cmndOutcome=cmndOutcome,
            )

        return cmndOutcome

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="parTypes",
            argDefault="all",               
            argChoices=['all', 'access', 'controllerInfo', 'submission'],
            argDescription="Action to be specified by rest"
        )

        return cmndArgsSpecDict
    

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "outMailAcctParsSet" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile outMailAcct userName userPasswd mtaRemHost mtaRemProtocol firstName lastName sendingMethod envelopeAddr" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<outMailAcctParsSet>>  =verify= parsOpt=bxoId sr controlProfile outMailAcct userName userPasswd mtaRemHost mtaRemProtocol firstName lastName sendingMethod envelopeAddr argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class outMailAcctParsSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'outMailAcct', 'userName', 'userPasswd', 'mtaRemHost', 'mtaRemProtocol', 'firstName', 'lastName', 'sendingMethod', 'envelopeAddr', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Optional Param
             sr: typing.Optional[str]=None,  # Cs Optional Param
             controlProfile: typing.Optional[str]=None,  # Cs Optional Param
             outMailAcct: typing.Optional[str]=None,  # Cs Optional Param
             userName: typing.Optional[str]=None,  # Cs Optional Param
             userPasswd: typing.Optional[str]=None,  # Cs Optional Param
             mtaRemHost: typing.Optional[str]=None,  # Cs Optional Param
             mtaRemProtocol: typing.Optional[str]=None,  # Cs Optional Param
             firstName: typing.Optional[str]=None,  # Cs Optional Param
             lastName: typing.Optional[str]=None,  # Cs Optional Param
             sendingMethod: typing.Optional[str]=None,  # Cs Optional Param
             envelopeAddr: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'outMailAcct': outMailAcct, 'userName': userName, 'userPasswd': userPasswd, 'mtaRemHost': mtaRemHost, 'mtaRemProtocol': mtaRemProtocol, 'firstName': firstName, 'lastName': lastName, 'sendingMethod': sendingMethod, 'envelopeAddr': envelopeAddr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        # cmndArgsSpec = {0: ['access', 'controllerInfo', 'submission']}

        # NOTYET
        parGroup = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        

        validParGroups = self.__class__.cmndArgsSpec[0]

        if not parGroup:
            parGroup = G.icmRunArgsGet().cmndArgs[0]

        if not parGroup in validParGroups:
            return b_io.eh.problem_usageError("mis-match")

        outMailAcctDir = os.path.join(
            outMailAcctDirGet(controlProfile, outMailAcct, bxoId=bxoId, sr=sr,),
        )

        if parGroup == "access":
            if userName:
                icm.b.fp.FileParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "userName"),
                    parValue=userName,
                )

            if userPasswd:                        
                icm.b.fp.FileParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "userPasswd"),
                    parValue=userPasswd,
                )

            if mtaRemHost:
                icm.b.fp.FileParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "mtaRemHost"),
                    parValue=mtaRemHost,
                )
                
            if mtaRemProtocol:
                icm.b.fp.FileParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "mtaRemProtocol"),
                    parValue=mtaRemProtocol,
                )
                
        elif parGroup == "controllerInfo":
            if firstName:                        
                icm.b.fp.FileParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "firstName"),
                    parValue=firstName,
                )

            if lastName:
                icm.b.fp.FileParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "lastName"),
                    parValue=lastName,
                )

        elif parGroup == "submission":
            if sendingMethod:                        
                icm.b.fp.FileParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "sendingMethod"),
                    parValue=sendingMethod,
                )

            if envelopeAddr:
                icm.b.fp.FileParamWriteToPath(
                    parNameFullPath=os.path.join(outMailAcctDir, parGroup, "envelopeAddr"),
                    parValue=envelopeAddr,
                )
            
        else:
            return b_io.eh.problem_usageError("OOPS")
        
        if rtInv.outs:
            icm.ANN_here(outMailAcctDir)

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=outMailAcctDir,
        )
    
    

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _ ~End Of Editable Text~ _: |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:

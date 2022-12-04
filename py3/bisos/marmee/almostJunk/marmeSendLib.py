# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* ::  A /library/ with ICM Cmnds to support ByStar facilities
"""

####+BEGIN: bx:cs:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
""" #+begin_org
*  This file:/bisos/git/auth/bxRepos/bisos-pip/marmee/py3/bisos/marmee/marmeSendLib.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
#+end_org """
####+END:


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "marmeSendLib"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "202210205540"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/csInfo-mbNedaGpl.py"

####+END:

####+BEGIN: bx:cs:python:topControls 
""" #+begin_org
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

"""
* 
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/pythonWb.org"
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "pep8 %s" (bx:buf-fname))))][pep8]] | [[elisp:(python-check (format "flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
####+END:
"""


####+BEGIN: bx:cs:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "insertPathForImports" :funcType "FrameWrk" :retType "none" :deco "" :argsList "path"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-FrameWrk [[elisp:(outline-show-subtree+toggle)][||]] /insertPathForImports/ retType=none argsList=(path)  [[elisp:(org-cycle)][| ]]
#+end_org """
def insertPathForImports(
    path,
):
####+END:
    """
** Extends Python imports path with  ../lib/python
"""
    import os
    import sys
    absolutePath = os.path.abspath(path)    
    if os.path.isdir(absolutePath):
        sys.path.insert(1, absolutePath)

insertPathForImports("../lib/python/")



####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=  [[elisp:(outline-show-subtree+toggle)][||]] *IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

import os
import collections
import enum

# NOTYET, should become a dblock with its own subItem
from unisos import ucf
from unisos import icm

G = cs.globalContext.get()
G.icmLibsAppend = __file__
G.csCmndsLibsAppend = __file__
# NOTYET DBLOCK Ends -- Rest of bisos libs follow;

from . import marmeAcctsLib

#import shlex
#import subprocess

#from datetime import datetime

#import re
#import pprint

import email
#import mailbox
#import smtplib

#import flufl.bounce

from unisos.x822Msg import msgOut
from unisos.x822Msg import msgIn


####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:python:icm:cmnd:classHead :modPrefix "new" :cmndName "bxpBaseDir_LibOverview" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 3 :pyInv ""

####+END:

        moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
This module is part of BISOS and its primary documentation is in  http://www.by-star.net/PLPC/180047
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""
        cmndArgsSpec = {"0&-1": ['moduleDescription', 'moduleUsage', 'moduleStatus']}
        cmndArgsValid = cmndArgsSpec["0&-1"]
        for each in effectiveArgsList:
            if each in cmndArgsValid:
                print(each)
                if rtInv.outs:
                    #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                    #version(interactive=True)
                    exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

####+BEGIN: bx:dblock:python:section :title "Support Functions For MsgProcs"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Support Functions For MsgProcs*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "sendCompleteMessage" :comment "" :parsMand "bxoId sr inFile" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "msg"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<sendCompleteMessage>>  =verify= parsMand=bxoId sr inFile ro=cli pyInv=msg   [[elisp:(org-cycle)][| ]]
#+end_org """
class sendCompleteMessage(cs.Cmnd):
    cmndParamsMandatory = [ 'bxoId', 'sr', 'inFile', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bxoId: typing.Optional[str]=None,  # Cs Mandatory Param
             sr: typing.Optional[str]=None,  # Cs Mandatory Param
             inFile: typing.Optional[str]=None,  # Cs Mandatory Param
             msg: typing.Any=None,   # pyInv Argument
    ) -> b.op.Outcome:

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'inFile': inFile, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return b_io.eh.badOutcome(cmndOutcome)
####+END:
        G = cs.globalContext.get()

        if not msg:
            if inFile:
                msg = msgIn.getMsgFromFile(inFile)
            else:
                # Stdin then
                msg = msgIn.getMsgFromStdin()
        else:
            # non-interactive call with msg
            if not bxoId:
                b_io.eh.problem_usageError("")
                return cmndOutcome
            
        b_io.tm.here(msgOut.strLogMessage(
            "Msg As Input:", msg,))

        b_io.tm.here(G.icmRunArgsGet().runMode)

        outcome = msgOut.sendingRunControlSet(msg, G.icmRunArgsGet().runMode)
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        bx822Set_setMandatoryFields(msg)

        outcome = bx822Get_sendingFieldsPipelineLoad(
            bxoId,
            sr,
            msg,
        )
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        if outcome.results != "INCOMPLETE":
            b_io.tm.here("Complete Message Being Sent")
            return (
                msgOut.sendBasedOnHeadersInfo(msg)
            )

        b_io.tm.here("Incomplete Message -- using qmail+dryrun")

        msgOut.injectionParams(
            msg,
            injectionProgram=msgOut.InjectionProgram.qmail,
            sendingRunControl=msgOut.SendingRunControl.dryRun,        
        )

        return msgOut.sendBasedOnHeadersInfo(msg)

        # return cmndOutcome.set(
        #     opError=b.OpError.Success,
        #     opResults=None,
        # )
    

####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(
####+END:
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  bx822Set_sendWithEnabledAcct    [[elisp:(org-cycle)][| ]]
"""
def bx822Set_sendWithEnabledAcct(
        bxoId,
        sr,
        msg,
        sendingMethod,
):
    """
** Setup BX-Send-WithControlProfile and BX-Send-WithAcctName to enabledAcct
"""
    if sendingMethod == msgOut.SendingMethod.inject:
        return True
    elif sendingMethod == msgOut.SendingMethod.submit:
        if not 'BX-Send-WithControlProfile' in msg:
            msg['BX-Send-WithControlProfile'] = marmeAcctsLib.enabledControlProfileObtain(
                bxoId=bxoId,
                sr=sr,
            )
        if not 'BX-Send-WithAcctName' in msg:
            msg['BX-Send-WithAcctName'] = marmeAcctsLib.enabledInMailAcctObtain(
                bxoId=bxoId,
                sr=sr,
            )
        return True
    else:
        return False
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  bx822Set_setMandatoryFields    [[elisp:(org-cycle)][| ]]
"""
def bx822Set_setMandatoryFields(
    msg,
):
    """
** Mail Sending Agent's Final Setups: Date, Message-ID, User-Agent, if needed
"""
    if not 'Date' in msg:
        msg['Date'] = email.utils.formatdate(localtime = 1)

    if not 'Message-ID' in msg:
        msg['Message-ID'] = email.utils.make_msgid()

    if not 'User-Agent' in msg:
        msg['User-Agent'] = "Marme/VersionNu"

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  bx822Get_sendingFieldsPipelineLoad    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def bx822Get_sendingFieldsPipelineLoad(
    bxoId,
    sr,
    msg,
):
    """
** Look for BX-Send-WithAcctName or BX-Send-WithBaseDir, and based on those prep the Bx822 fields.
"""
    opOutcome = b.op.Outcome()
    if 'BX-Send-WithAcctName' in msg:
        controlProfile = msg['BX-Send-WithControlProfile']
        outMailAcct = msg['BX-Send-WithAcctName']
        return (
            msgSendingPipelineLoadFromAcct(
                bxoId,
                sr,
                msg,
                controlProfile,
                outMailAcct,
            ))
    elif 'BX-Send-WithBaseDir' in msg:
        acctBaseDir = msg['BX-Send-WithBaseDir']
        return (
            msgSendingPipelineLoadFromAcctBaseDir(
                msg,
                acctBaseDir,
            ))
    else:
        return opOutcome.set(opResults='INCOMPLETE')


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  msgSendingPipelineLoadFromAcct    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def msgSendingPipelineLoadFromAcct(
        bxoId,
        sr,
        msg,
        controlProfile,
        outMailAcct,
):
    """
** Just call with obtained base for acct.
    """
    acctBaseDir = marmeAcctsLib.outMailAcctDirGet(
        controlProfile,
        outMailAcct,
        bxoId=bxoId,
        sr=sr,
    )
    return (
        msgSendingPipelineLoadFromAcctBaseDir(
            msg,
            acctBaseDir,
        ))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  msgSendingPipelineLoadFromAcctBaseDir    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def msgSendingPipelineLoadFromAcctBaseDir(
        msg,
        acctBaseDir,
):
    """
** Read File Params for mailAcct and set X822-MSP params accordingly
    """
    opOutcome = b.op.Outcome()
    #print acctBaseDir
    #G = cs.globalContext.get()

    outcome = icm.FP_readTreeAtBaseDir().cmnd(
        interactive=False,
        FPsDir=os.path.join(acctBaseDir, 'access'),
    )
    fp_access_dict = outcome.results

    outcome = icm.FP_readTreeAtBaseDir().cmnd(
        interactive=False,
        FPsDir=os.path.join(acctBaseDir, 'controllerInfo'),
    )
    #fp_controllerInfo_dict = outcome.results
    
    outcome = icm.FP_readTreeAtBaseDir().cmnd(
        interactive=False,
        FPsDir=os.path.join(acctBaseDir, 'submission'),
    )
    fp_submission_dict = outcome.results

    envelopeAddr = fp_submission_dict["envelopeAddr"].parValueGet()
    
    msgOut.envelopeAddrSet(
        msg,
        mailBoxAddr=envelopeAddr,  # Mandatory
    )

    sendingMethod = fp_submission_dict["sendingMethod"].parValueGet()

    if msgOut.sendingMethodSet(msg, sendingMethod).isProblematic():
        return b_io.eh.badLastOutcome()

    if sendingMethod == msgOut.SendingMethod.inject:
        return opOutcome

    #
    # So, It is a submission 
    #
    # NOTYET, below should be split and use
    #  msgOut.submitParamsNOT()
    #

    try:
        mtaRemHost = fp_access_dict["mtaRemHost"].parValueGet()
    except  KeyError:
        return icm.eh_problem_usageError_wOp(opOutcome, "Missing BX-MTA-Rem-Host")

    try:
        userName = fp_access_dict["userName"].parValueGet()
    except  KeyError:
        return icm.eh_problem_usageError_wOp(opOutcome, "Missing BX-MTA-Rem-User")

    try:
        userPasswd = fp_access_dict["userPasswd"].parValueGet()
    except  KeyError:
        return icm.eh_problem_usageError_wOp(opOutcome, "Missing BX-MTA-Rem-Passwd")

    try:
        remProtocol = fp_access_dict["mtaRemProtocol"].parValueGet()        
    except  KeyError:
        return icm.eh_problem_usageError_wOp(opOutcome, "Missing BX-MTA-Rem-Protocol")
    
    try:
        remPortNu = fp_access_dict["mtaRemPortNu"].parValueGet()
    except  KeyError:
        remPortNu = None

    msgOut.submitParams(
        msg,
        mtaRemProtocol=remProtocol,          # smtp
        mtaRemHost=mtaRemHost,              # Remote Host To Submit to (could be localhost)
        mtaRemPort=remPortNu,
        mtaRemUser=userName,        
        mtaRemPasswd=userPasswd,
        mtaRemCerts=None,
    )
    
    return opOutcome
    
    

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _ ~End Of Editable Text~ _: |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:

"""Subclass of MorphologyDlg, which is generated by wxFormBuilder."""

import cv2
import wx

import CL
import UCommon

# Implementing MorphologyDlg
class UMorphologyDlg( CL.MorphologyDlg ):
	def __init__( self, parent ):
		CL.MorphologyDlg.__init__( self, parent )

	# Handlers for MorphologyDlg events.
	def OnCancel( self, event ):
		# TODO: Implement OnCancel
		self.EndModal(0)

	def OnPreView( self, event ):
		# TODO: Implement OnPreView
		self.Execute(False)

	def OnExec( self, event ):
		# TODO: Implement OnExec
		self.Execute(True)
		self.EndModal(1)

	def Execute(self, Flag):
		"""処理実行
		"""
		op_code = self.m_radioBox2.GetSelection()
		ksize   = self.m_spinCtrl44.GetValue()
		it      = self.m_spinCtrl37.GetValue()
		if op_code   == 0:
			op = cv2.MORPH_ERODE
		elif op_code == 1:
			op = cv2.MORPH_DILATE
		elif op_code == 2:
			op = cv2.MORPH_OPEN
		elif op_code == 3:
			op = cv2.MORPH_CLOSE
		elif op_code == 4:
			op = cv2.MORPH_GRADIENT
		elif op_code == 5:
			op = cv2.MORPH_TOPHAT
		elif op_code == 6:
			op = cv2.MORPH_BLACKHAT
		if Flag:
			self.cv_image = self.cv_image.morphologyEx(op, ksize, it)
			self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
		else:
			ret_img = self.cv_image.morphologyEx(op, ksize, it)
			self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))

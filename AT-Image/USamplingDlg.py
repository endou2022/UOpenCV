"""Subclass of SamplingDlg, which is generated by wxFormBuilder."""

import wx

import CL
import UCommon

# Implementing SamplingDlg
class USamplingDlg( CL.SamplingDlg ):
	def __init__( self, parent ):
		CL.SamplingDlg.__init__( self, parent )

	# Handlers for SamplingDlg events.
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
		upper = self.m_colourPicker1.GetColour()  # カラーは color(米国英語) ではなく colour(英国英語) であることに注意
		lower = self.m_colourPicker5.GetColour()

		if Flag:
			self.cv_image = self.cv_image.sampling_bgr(lower , upper)
			self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
		else:
			ret_img = self.cv_image.sampling_bgr(lower , upper)
			self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
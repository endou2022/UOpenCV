"""Subclass of ShadingDlg, which is generated by wxFormBuilder."""

import wx

import CL
import UCommon
from UOpenCV import UOpenCV

# Implementing ShadingDlg
class UShadingDlg( CL.ShadingDlg ):
	def __init__( self, parent ):
		CL.ShadingDlg.__init__( self, parent )

	# Handlers for ShadingDlg events.
	def OnCancel( self, event ):
		# TODO: Implement OnCancel
		self.EndModal(0)

	def OnPreView( self, event ):
		# TODO: Implement OnPreView
		self.Execute(False)

	def OnExec( self, event ):
		# TODO: Implement OnExec
		ret = self.Execute(True)
		if ret:
			self.EndModal(1)

	def Execute(self, Flag):
		"""処理実行
		"""
		page = self.m_notebook1.GetSelection()
		if   page == 0:  # 黒基準画像
			b_fname = self.m_filePicker3.GetPath()
			offset  = self.m_spinCtrlDouble1.GetValue()
			if b_fname == '':
				wx.MessageBox('黒基準画像ファイルが指定されていません', 'エラー', wx.ICON_ERROR)
				return False
			try:
				black_reference = UOpenCV(b_fname)
				if Flag:
					self.cv_image = self.cv_image.shading_black(black_reference, offset)
					self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
				else:
					ret_img = self.cv_image.shading_black(black_reference, offset)
					self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
			except Exception as e:
				wx.MessageBox(str(e), 'エラー', wx.ICON_ERROR)
				return False
			return True

		elif page == 1:  # 白・黒基準画像
			w_fname = self.m_filePicker311.GetPath()  #白
			b_fname = self.m_filePicker31.GetPath()   #黒
			multi   = self.m_spinCtrlDouble2.GetValue()
			if b_fname == '':
				wx.MessageBox('黒基準画像ファイルが指定されていません', 'エラー', wx.ICON_ERROR)
				return False
			if w_fname == '':
				wx.MessageBox('白基準画像ファイルが指定されていません', 'エラー', wx.ICON_ERROR)
				return False
			try:
				black_reference = UOpenCV(b_fname)
				white_reference = UOpenCV(w_fname)
				if Flag:
					self.cv_image = self.cv_image.shading_white_black(white_reference, black_reference, multi)
					self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
				else:
					ret_img = self.cv_image.shading_white_black(white_reference, black_reference, multi)
					self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
			except Exception as e:
				wx.MessageBox(str(e), 'エラー', wx.ICON_ERROR)
				return False
			return True

		elif page == 2:  # 凸凹係数
			ksize = self.m_spinCtrl41.GetValue()
			if Flag:
				self.cv_image = self.cv_image.shading_unevenness(ksize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.shading_unevenness(ksize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
			return True

		elif page == 3:  # モルフォロジー演算
			ksize = self.m_spinCtrl412.GetValue()
			if Flag:
				self.cv_image = self.cv_image.shading_blackhat(ksize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(self.cv_image, self.magnification))
			else:
				ret_img = self.cv_image.shading_blackhat(ksize)
				self.bitmap.SetBitmap(UCommon.uopencv2wxbitmap(ret_img, self.magnification))
			return True
"""Subclass of GWin, which is generated by wxFormBuilder."""

import copy

import wx

import CL
import UCommon
from UOpenCV import UOpenCV
from URubberBand import URubberBand

# Implementing GWin
class UGWin(URubberBand, CL.GWin ):
	def __init__( self, parent ):
		CL.GWin.__init__( self, parent )
		URubberBand.__init__(self, self.m_bitmap1)
		self.parent = parent  # 親ウインドウの関数を使うため

	# Handlers for GWin events.
	def OnMvEnd( self, event ):
		# TODO: Implement OnMvEnd
		pos = self.GetPosition()
		self.parent.ChildWinPoint = pos + wx.Point(20,20)

	def OnOpen( self, event ):
		# TODO: Implement OnOpen
		self.parent.OpenImgFile()

	def OnSaveAs( self, event ):
		# TODO: Implement OnSaveAs
		UCommon.SaveAs(self)

	def OnWClose( self, event ):
		# TODO: Implement OnWClose
		self.Close()

	def OnExit( self, event ):
		# TODO: Implement OnExit
		self.parent.OnExit(event)

	def OnCopy( self, event ):
		# TODO: Implement OnCopy
		UCommon.CopyToClipboard(self.cv_image)

	def OnPaste( self, event ):
		# TODO: Implement OnPaste
		self.parent.CopyFromClipboard()

	def OnZoomIn( self, event ):
		# TODO: Implement OnZoomIn
		UCommon.ZoomIn(self)

	def OnZoomOut( self, event ):
		# TODO: Implement OnZoomOut
		UCommon.ZoomOut(self)

	def OnZoomRst( self, event ):
		# TODO: Implement OnZoomRst
		UCommon.ZoomRst(self)

	def OnViewLog( self, event ):
		# TODO: Implement OnViewLog
		self.parent.LogDlg.DispLog(self.cv_image)

	def OnMono( self, event ):
		# TODO: Implement OnMono
		win = self.parent.NewColorWindow(self.cv_image, self.magnification)  # 新しい画像を作って
		self.parent.MonoDlg.cv_image = win.cv_image      # ダイアローグにUOpenCVオブジェクトとwx.StaticBitmapオブジェクトを渡す (参照渡しのはずなのだが)
		self.parent.MonoDlg.bitmap   = win.m_bitmap1
		self.parent.MonoDlg.magnification = win.magnification
		ret = self.parent.MonoDlg.ShowModal()            # モーダルダイアローグとして開く
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.MonoDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnPseud( self, event ):
		# TODO: Implement OnPseud
		win = self.parent.NewColorWindow(self.cv_image, self.magnification)
		self.parent.PseudDlg.cv_image = win.cv_image
		self.parent.PseudDlg.bitmap   = win.m_bitmap1
		self.parent.PseudDlg.magnification = win.magnification
		ret = self.parent.PseudDlg.ShowModal()
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.PseudDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnBinary( self, event ):
		# TODO: Implement OnBinary
		win = self.parent.NewBinWindow(self.cv_image, self.magnification)
		self.parent.BinaryDlg.cv_image = win.cv_image
		self.parent.BinaryDlg.bitmap   = win.m_bitmap1
		self.parent.BinaryDlg.magnification = win.magnification
		self.parent.BinaryDlg.ShowHist()
		ret = self.parent.BinaryDlg.ShowModal()
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.BinaryDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnFFT( self, event ):
		# TODO: Implement OnFFT
		self.parent.NewEtcWindow(self.cv_image.dft(), self.magnification)
		self.parent.SetWinTitle(self)

	def OnChHist( self, event ):
		# TODO: Implement OnChHist
		win = self.parent.NewGrayWindow(self.cv_image, self.magnification)
		self.parent.ChHistDlg.cv_image = win.cv_image
		self.parent.ChHistDlg.bitmap   = win.m_bitmap1
		self.parent.ChHistDlg.magnification = win.magnification
		self.parent.ChHistDlg.ShowHist()
		ret = self.parent.ChHistDlg.ShowModal()
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.ChHistDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnFilter( self, event ):
		# TODO: Implement OnFilter
		win = self.parent.NewGrayWindow(self.cv_image, self.magnification)
		self.parent.FilterDlg.cv_image = win.cv_image
		self.parent.FilterDlg.bitmap   = win.m_bitmap1
		self.parent.FilterDlg.magnification = win.magnification
		ret = self.parent.FilterDlg.ShowModal()
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.FilterDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnLookup( self, event ):
		# TODO: Implement OnLookup
		win = self.parent.NewGrayWindow(self.cv_image, self.magnification)
		self.parent.LookUpDlg.cv_image = win.cv_image
		self.parent.LookUpDlg.bitmap   = win.m_bitmap1
		self.parent.LookUpDlg.magnification = win.magnification
		ret = self.parent.LookUpDlg.ShowModal()
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.LookUpDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnMorphology( self, event ):
		# TODO: Implement OnMorphology
		win = self.parent.NewGrayWindow(self.cv_image, self.magnification)
		self.parent.MorphologyDlg.cv_image = win.cv_image
		self.parent.MorphologyDlg.bitmap   = win.m_bitmap1
		self.parent.MorphologyDlg.magnification = win.magnification
		ret = self.parent.MorphologyDlg.ShowModal()
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.MorphologyDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnContours( self, event ):
		# TODO: Implement OnContours
		win = self.parent.NewBinWindow(self.cv_image, self.magnification)
		self.parent.ContoursDlg.cv_image = win.cv_image
		self.parent.ContoursDlg.bitmap   = win.m_bitmap1
		self.parent.ContoursDlg.magnification = win.magnification
		ret = self.parent.ContoursDlg.ShowModal()
		# Contoursだけ特別
		if ret == 0:
			win.Destroy()
		elif ret == 3:  # モルフォロジー(GRADIENT)処理で境界を求めた場合
			win.Destroy()
			win = self.parent.NewGrayWindow(self.parent.ContoursDlg.cv_image, self.parent.ContoursDlg.magnification)
			self.parent.SetWinTitle(win)
		else:
			win.cv_image = copy.deepcopy(self.parent.ContoursDlg.cv_image)
			self.parent.SetWinTitle(win)

	def OnEdge( self, event ):
		# TODO: Implement OnEdge
		win = self.parent.NewColorWindow(self.cv_image, self.magnification)  # カラー画像に変換している
		self.parent.EdgeDlg.cv_image = win.cv_image
		self.parent.EdgeDlg.bitmap   = win.m_bitmap1
		self.parent.EdgeDlg.magnification = win.magnification
		ret = self.parent.EdgeDlg.ShowModal()
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.EdgeDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnArt( self, event ):
		# TODO: Implement OnArt
		win = self.parent.NewGrayWindow(self.cv_image, self.magnification)
		self.parent.ArtDlg.cv_image = win.cv_image
		self.parent.ArtDlg.bitmap   = win.m_bitmap1
		self.parent.ArtDlg.magnification = win.magnification
		ret = self.parent.ArtDlg.ShowModal()
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.ArtDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnOp( self, event ):
		# TODO: Implement OnOp
		self.parent.OpDlg.SetChoice(self.GetTitle())
		win = self.parent.NewColorWindow(self.cv_image, self.magnification)
		self.parent.OpDlg.cv_image = win.cv_image
		self.parent.OpDlg.bitmap   = win.m_bitmap1
		self.parent.OpDlg.magnification = win.magnification
		ret = self.parent.OpDlg.ShowModal()
		if ret == 1:
			win.cv_image = copy.deepcopy(self.parent.OpDlg.cv_image)
			self.parent.SetWinTitle(win)
		else:
			win.Destroy()

	def OnHist( self, event ):
		# TODO: Implement OnHist
		self.cv_image.calcHist()
		self.parent.RetDlg.HistResult(self.cv_image)
		UCommon.showHist(self.cv_image)

	def OnDistH( self, event ):
		# TODO: Implement OnDistH
		self.cv_image.projection_distribution_h()
		self.parent.RetDlg.DistResult(self.cv_image)
		UCommon.showDist(self.cv_image)

	def OnDistV( self, event ):
		# TODO: Implement OnDistV
		self.cv_image.projection_distribution_v()
		self.parent.RetDlg.DistResult(self.cv_image)
		UCommon.showDist(self.cv_image)

	def OnHistArea( self, event ):
		# TODO: Implement OnHistArea
		self.SetCursor(wx.Cursor(wx.CURSOR_CROSS))
		self.draw_type = URubberBand.Rectangle
		self.func_type = URubberBand.HistArea

	def OnDistHArea( self, event ):
		# TODO: Implement OnDistHArea
		self.SetCursor(wx.Cursor(wx.CURSOR_CROSS))
		self.draw_type = URubberBand.Rectangle
		self.func_type = URubberBand.DistHArea

	def OnDistVArea( self, event ):
		# TODO: Implement OnDistVArea
		self.SetCursor(wx.Cursor(wx.CURSOR_CROSS))
		self.draw_type = URubberBand.Rectangle
		self.func_type = URubberBand.DistVArea

	def OnLine( self, event ):
		# TODO: Implement OnLine
		self.SetCursor(wx.Cursor(wx.CURSOR_CROSS))
		self.draw_type = URubberBand.Line
		self.func_type = URubberBand.DistLine

	def OnPixcel( self, event ):
		# TODO: Implement OnPixcel
		self.parent.PixDlg.Show(True)

	def OnAbout( self, event ):
		# TODO: Implement OnAbout
		UCommon.About()

	def OnLDwn( self, event ):
		# TODO: Implement OnLDwn
		if self.parent.PixDlg.IsShown():  # ピクセル表示ならば
			pos = event.GetPosition()
			x = int(pos.x / self.magnification)
			y = int(pos.y / self.magnification)
			self.parent.PixDlg.View(self, x, y)
		if self.draw_type != URubberBand.NoRubber:
			URubberBand.OnMLDown(self,  event )

	def OnLUp( self, event ):
		# TODO: Implement OnLUp
		if self.drag_flag:
			URubberBand.OnMLUp( self, event )
			self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
			bx = int(self.begin_pos.x / self.magnification)
			by = int(self.begin_pos.y / self.magnification)
			ex = int(self.end_pos.x   / self.magnification)
			ey = int(self.end_pos.y   / self.magnification)
			if   self.func_type == URubberBand.HistArea:
				self.cv_image.calcHist(bx, by, ex, ey)
				self.parent.RetDlg.HistResult(self.cv_image, bx, by, ex, ey)
				UCommon.showHist(self.cv_image)
			elif self.func_type == URubberBand.DistHArea:
				self.cv_image.projection_distribution_h(bx, by, ex, ey)
				self.parent.RetDlg.DistResult(self.cv_image, bx, by, ex, ey)
				UCommon.showDist(self.cv_image)
			elif self.func_type == URubberBand.DistVArea:
				self.cv_image.projection_distribution_v(bx, by, ex, ey)
				self.parent.RetDlg.DistResult(self.cv_image, bx, by, ex, ey)
				UCommon.showDist(self.cv_image)
			elif self.func_type == URubberBand.DistLine:
				self.cv_image.get_line_data(bx, by, ex, ey)
				self.parent.RetDlg.GetLineResult(self.cv_image, bx, by, ex, ey)
				UCommon.showLine(self.cv_image)

	def OnMove( self, event ):
		# TODO: Implement OnMove
		if self.drag_flag:
			if self.parent.PixDlg.IsShown():  # ピクセル表示ならば
				pos = event.GetPosition()
				x = int(pos.x / self.magnification)
				y = int(pos.y / self.magnification)
				self.parent.PixDlg.View(self, x, y)
			URubberBand.OnMMotion( self, event )
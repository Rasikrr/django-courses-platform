class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context["title"] = self.title
        return context


class MenuMixin:
    menu_section = None

    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context["menu_section"] = self.menu_section
        return context
from odoo import api, models, fields
from datetime import date

class BookDetails(models.Model):
    _name = 'book.details'
    _description = 'Book Details'

    title = fields.Char(string='Title' , required=True)
    author = fields.Char(string='Author')
    publisher = fields.Char(string='Publisher')
    published_date = fields.Date(string='Published Date')
    book_age = fields.Integer(string='Book Age' , compute='_compute_book_age', store=True)
    genre = fields.Selection([
    ('romance', 'Romance'),
    ('adventure', 'Adventure'),
    ('sci_fi', 'Sci-Fi'),
], string='Genre')

    @api.depends('published_date')
    def _compute_book_age(self):
        for record in self:
            if record.published_date:
                record.book_age = date.today().year - record.published_date.year
            
            else:
                record.book_age = 0
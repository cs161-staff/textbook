---
title: Glossary
nav_order: 6
---

# Glossary

<table class="grid" style="width: 100%">
    <colgroup>
        <col width="20%" />
        <col width="70%" />
        <col width="10%" />
    </colgroup>
    <thead>
        <tr class="header">
            <th>Term</th>
            <th>Definition</th>
            <th>Chapter</th>
        </tr>
    </thead>
    <tbody>
    {% for entry in site.data.glossary %}
        <tr>
          <td>{{ entry.term }}</td>
          <td>{{ entry.definition }}</td>
          <td>{{ entry.chapter }}</td>
        </tr>
    {% endfor %}
    </tbody>
</table>
